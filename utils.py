import requests
import config
from datetime import datetime
from datetime import timezone


listed_cryptos = list(config.crypto_color_config.keys())

def get_info(slug):
    #make the request, get the json
    params = {"slug":slug}
    r = requests.get(url=config.URL, headers=config.headers, params=params, timeout=30)
    
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
                image = f"{config.IMAGE_URL}{coin_id}.png"
        
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
    response = requests.post(config.WEBHOOK_URL, json=data, timeout=30)

    if response.status_code >= 400:
        print(f"Failed to send to discord webhook, {response.text}")
    
    else:
        print(f"Price information for {title} sent to webhook.")