# Hospital Appointment Notifier 🏥🤖

An automated web-scraping bot that monitors the **Wanfang Hospital** appointment system and sends real-time notifications to a Discord channel when specific slots become available.

-----

## 🚀 Features

  * **Automated Monitoring**: Continuously checks for appointment availability on a loop.
  * **Discord Integration**: Sends instant alerts to your Discord server so you don't have to refresh the browser.
  * **Multi-Date Tracking**: Iterates through multiple target date buttons to find open slots.
  * **Asynchronous Execution**: Uses `discord.ext.tasks` to ensure the bot remains online while the scraper runs in the background.

## 🛠️ Tech Stack

| Tool | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **Selenium** | Browser automation & Dynamic content scraping |
| **Discord.py** | Bot API integration & Notifications |
| **Chrome WebDriver** | Interface between Selenium and the Chrome browser |

-----

## ✨ Result

1.  **Video Demo**

    [Watch the video](https://youtu.be/L5bApQqDMNc)

-----

## ⚙️ Configuration

Open the script and update the following variables:

```python
# Discord Bot Token
API = 'YOUR_BOT_TOKEN_HERE'

# The ID of the channel where the bot should post alerts
CHANNEL_ID = 'YOUR_CHANNEL_ID_HERE' 

# Target Hospital URL
URL = "https://wwww.wanfang.gov.tw/..."
```

-----

## 🖥️ Methodology 

Run the script using Python:

```bash
python "Hospital Appointment Notifier.py"
```

The bot will:

1.  Log into Discord.
2.  Open a Chrome instance.
3.  Navigate to the Wanfang Hospital registration page.
4.  Cycle through the date buttons provided in `date_button_ids`.
5.  If an appointment button (`.btn-large`) is found, it pings the specified Discord channel.

-----

## 📜 Disclaimer

This project is for **educational purposes only**. Please be mindful of the website's `robots.txt` and Terms of Service. Frequent scraping may result in an IP ban. Use responsibly.

-----

*Made with ❤️ for easier healthcare access.*
