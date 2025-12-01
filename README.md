<ins>Crypto Price Monitor</ins>

A Python script that retrieves cryptocurrency price data from the CoinMarketCap API and posts formatted updates to a Discord channel using webhooks.
This project was created to practice working with HTTP requests, APIs, environment variables, and basic automation.
<hr>
<ins>Requirements</ins>
<p>&nbsp;</p>

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
<hr>
<ins>Setup</ins>
<p>&nbsp;</p>


*1. CoinMarketCap API Key*

>Create an account and generate an <a href="https://coinmarketcap.com/api/">API key</a>

*2. Discord Webhook*

Create a <a href="https://coinmarketcap.com/api/">webhook</a>:

3. Environment Variables

Create a .env file in the project directory:

```bash
KEY="your_coinmarketcap_api_key_here"
DISCORD_WEBHOOK="your_discord_webhook_url_here"
```
<sub>Make sure `.env` is in your `.gitignore`.</sub>	
<hr>
<ins>Configuration</ins>
<p>&nbsp;</p>

Edit cryptocurrency tracking in:
```py
crypto_color_config = {
    "bitcoin": 16744192,
    "ethereum": 6449295,
    "xrp": 0,
    "bnb": 16744192,
    "solana": 7602431
}
```

Notes:

<li>Keys must be valid CoinMarketCap slugs</li>
<li>Values are Discord embed color integers.</li>
<li>Add or remove entries as desired.</li>

<hr>
<ins>Running the Script</ins>
<p>&nbsp;</p>
  
Run the script:
```py
python main.py
```

The script will:

<li>Load API keys from .env</li>

<li>Fetch crypto data from CoinMarketCap</li>

<li>Send an embed to your Discord webhook</li>

<li>Rotate to the next crypto every 60 seconds</li>
<hr>
<ins>Notes</ins>
<p>&nbsp;</p>

```
- Timestamps are sent in UTC for accurate Discord display.
- All API failures and exceptions print to the console.
- This project is meant as a simple API + automation practice script.
```