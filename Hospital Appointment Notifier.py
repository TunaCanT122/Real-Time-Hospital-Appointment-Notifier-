import discord
from discord.ext import tasks
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio

API = 'YOUR_API_HERE' # Remove the { } brackets
CHANNEL_ID = 'YOUR_CHANNEL_ID_HERE'  # You need the ID of the channel where the bot should post

class AppointmentBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize the driver once
        self.driver = webdriver.Chrome() 

    async def setup_hook(self):
        # Start the background scraping task
        self.scraper_task.start()

    async def on_ready(self):
        print(f'Logged in as {self.user}')

    @tasks.loop(seconds=60)
    async def scraper_task(self):
        # This function runs every 60 seconds automatically
        print("Checking for appointments...")
        try:
            self.driver.get("https://wwww.wanfang.gov.tw/reg/register_ec_cload2.aspx?pidm=E3F7A20668DEB951D52D97CA8F059AA2")
            
            date_button_ids = ["ContentPlaceHolder1_ButtonDate1", "ContentPlaceHolder1_ButtonDate2"]
            
            for button_id in date_button_ids:
                try:
                    button = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.ID, button_id))
                    )
                    button.click()
                    await asyncio.sleep(2) # Give it a moment to load
                    
                    targets = self.driver.find_elements(By.CSS_SELECTOR, "a.waves-effect.waves-light.indigo.btn-large")
                    
                    if len(targets) > 0:
                        channel = self.get_channel(CHANNEL_ID)
                        for target in targets:
                            await channel.send(f"Appointment Found: {target.text}")
                            
                except Exception as e:
                    print(f"Error clicking {button_id}: {e}")
                    
        except Exception as e:
            print(f"Scraper encountered an error: {e}")

intents = discord.Intents.default()
client = AppointmentBot(intents=intents)
client.run(API)
