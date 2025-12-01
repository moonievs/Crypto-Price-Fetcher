import requests
from datetime import datetime, timedelta, timezone
import os
import time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("KEY")
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
if not API_KEY:
    raise Exception("API Key does not exist in .env file, make sure to fetch a valid CMC API Key here: https://coinmarketcap.com/api/")
if not WEBHOOK_URL:
    raise Exception("Discord Webhook not present, refer to: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks")

URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
IMAGE_URL = "https://s2.coinmarketcap.com/static/img/coins/64x64/"

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': API_KEY,
}

crypto_color_config = {
    "bitcoin": 16744192,
    "ethereum": 6449295,
    "xrp": 0,
    "bnb": 16744192,
    "solana": 7602431
}

def get_info(slug):
    #make the request, get the json
    params = {"slug":slug}
    r = requests.get(url=URL, headers=headers, params=params, timeout=30)
    
    if r.status_code == 200: # check for positive status
        crypto_data = r.json()

        if crypto_data["status"]["error_code"] == 0:
             
            if not crypto_data["data"]:
                raise Exception(f"There are no valid keys in the data json, likely because {slug} information does not exist.")
            # if success, set price value using json response
            else:
                coin_id = list(crypto_data["data"].keys())[0]
                data_location = crypto_data["data"][coin_id]["quote"]["USD"]

                price = data_location["price"]
                last_24_hr = data_location["percent_change_24h"]
                last_seven_days = data_location["percent_change_7d"]
                image = f"{IMAGE_URL}{coin_id}.png"
        
        else:    # check reponse status (CMC response contains own status & errors)
            raise Exception(f"Fetch for {slug} failed: {crypto_data['status']['error_message']}") #raise CMC error message

    else:
        raise Exception(f"Failed to get Status 200, instead got {r.status_code} because of ")

    return price, last_24_hr, last_seven_days, image

def discord_message(title:str, price:str, last_24_hours:str, last_seven_days:str, image:str, color):
    """params: 

    - slug: the colour for the embed"""
    embed = {
        "title": f"{title.title()}'s Price",
        "description": f"{price}\n\n**Last 24 Hours:** {last_24_hours}%\n**Last 7 Days: **{last_seven_days}%",
        "thumbnail": {"url": image},
        "footer": {"text": "Crypto Price Monitor"},
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "color": color
    }

    data = {
        "embeds": [embed]
    }
    response = requests.post(WEBHOOK_URL, json=data, timeout=30)

    if response.status_code >= 400:
        print(f"Failed to send to discord webhook, {response.text}")
    
    else:
        print(f"Price information for {title} sent to webhook.")

if __name__ == "__main__":
    last_run = datetime.now() - timedelta(seconds=60)
    count = 0
    listed_cryptos = list(crypto_color_config.keys())
    while True:
        now = datetime.now()
        crypto = listed_cryptos[count]
        
        # Check if 60 seconds have passed
        if (now - last_run).total_seconds() >= 60:
            try:
                price, last_24, last_7, image = get_info(crypto)
                formatted_price = f"${price:,.2f}"
                formatted_last_24 = f"{last_24:,.2f}"
                formatted_last_7 = f"{last_7:,.2f}"
                color = crypto_color_config[crypto]

                discord_message(crypto, formatted_price, formatted_last_24, formatted_last_7, image, color)

            except Exception as e:
                print(e)

            # Reset the timer AFTER running the task
            count+=1
            if count == len(listed_cryptos):
                count=0
            last_run = datetime.now()

        time.sleep(5)  # Check every 5 seconds