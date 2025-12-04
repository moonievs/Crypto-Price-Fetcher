import os
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


CRYPTO_COLOR_CONFIG = {
    "bitcoin": 16744192,
    "ethereum": 6449295,
    "xrp": 0,
    "bnb": 16744192,
    "solana": 7602431
}