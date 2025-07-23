import discord
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#discord online
#Enter Discord Bot API here
API=''

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)



driver.get("https://wwww.wanfang.gov.tw/reg/register_ec_cload2.aspx?pidm=E3F7A20668DEB951D52D97CA8F059AA2")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btn"))
)




# Target button values
date_button_ids = [
    "ContentPlaceHolder1_ButtonDate1",
    "ContentPlaceHolder1_ButtonDate2",
    "ContentPlaceHolder1_ButtonDate3",
    "ContentPlaceHolder1_ButtonDate4"
]

class Client(discord.Client):
  async def on_ready(self):
    print(f'!!!!!!!!!!!!!!!!!we have logged in as {self.user}!')

  async def on_message(self, message):
      if print(len(targets)) != 0:
          await message.channel.send(f'{target.text}')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

client.run({API})



for i in range(1880):
    print(f"Loop {i + 1}")

    for button_id in date_button_ids:
        try:

            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, button_id))
            )
            button.click()
            print("Clicked on:", button_id)
            time.sleep(8)
        except Exception as e:
            print(f"❌ Failed to click on '{button_id}': {e}") #ContentPlaceHolder1_ButtonDate3
        targets = driver.find_elements(By.CSS_SELECTOR, "a.waves-effect.waves-light.indigo.btn-large")
        for target in targets:
            print(len(targets))
            print(target.text)
            async def on_message(self, message):
                if print(len(targets))!=0:
                    await message.channel.send(f'{target.text}')

    print("✅ Waiting 60 seconds before next loop...\n")
    time.sleep(60)
