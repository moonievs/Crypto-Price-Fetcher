# Crypto Price Monitor

A Python script that retrieves cryptocurrency price data from the CoinMarketCap API and posts formatted updates to a Discord channel using webhooks. This project was created to practice working with HTTP requests, APIs, environment variables, and basic automation.

---

## Requirements

Python 3.10+

Install dependencies:

```bash
pip install -r requirements.txt
```

Required packages:

```
requests
python-dotenv
```

---

## Setup

### CoinMarketCap API Key
Create an account and generate an API key:  
https://coinmarketcap.com/api/

### Discord Webhook
Create a webhook in your Discord server.

### Environment Variables
Create a `.env` file in the project directory:

```env
KEY="your_coinmarketcap_api_key_here"
DISCORD_WEBHOOK="your_discord_webhook_url_here"
```

---

## Configuration

Edit cryptocurrency tracking in:

```python
crypto_color_config = {
    "bitcoin": 16744192,
    "ethereum": 6449295,
    "xrp": 0,
    "bnb": 16744192,
    "solana": 7602431
}
```

Notes:

- Keys must be valid CoinMarketCap slugs  
- Values are Discord embed color integers  
- Add or remove entries as desired  

---

## Running the Script

Run the script:

```bash
python main.py
```

The script will:

- Load API keys from `.env`
- Fetch crypto data from CoinMarketCap
- Send an embed to your Discord webhook
- Rotate to the next crypto every 60 seconds

---

## Notes

```
- Timestamps are sent in UTC for accurate Discord display.
- All API failures and exceptions print to the console.
- This project is meant as a simple API + automation practice script.
```
