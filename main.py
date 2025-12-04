from datetime import datetime 
from datetime import timedelta
import time
import utils

if __name__ == "__main__":
    last_run = datetime.now() - timedelta(seconds=60)
    count = 0
    while True:
        now = datetime.now()
        crypto = utils.listed_cryptos[count]
        
        # Check if 60 seconds have passed
        if (now - last_run).total_seconds() >= 60:
            try:
                price, last_24, last_7, image = utils.get_info(crypto)
                formatted_price = f"${price:,.2f}"
                formatted_last_24 = f"{last_24:,.2f}"
                formatted_last_7 = f"{last_7:,.2f}"
                color = utils.config.crypto_color_config[crypto]

                utils.discord_message(crypto, formatted_price, formatted_last_24, formatted_last_7, image, color)

            except Exception as e:
                print(e)

            # Reset the timer AFTER running the task
            count+=1
            if count == len(utils.listed_cryptos):
                count=0
            last_run = datetime.now()

        time.sleep(5)  # Check every 5 seconds