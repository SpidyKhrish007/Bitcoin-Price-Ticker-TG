import os

from dotenv import load_dotenv

load_dotenv()
# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "1747534"))
API_HASH = os.environ.get("API_HASH", "5a2684512006853f2e48aca9652d83ea")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6492737948:AAGBOytQGoq6xXNyC-CTRHYTFkO70FiThtQ")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001604178274"))
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", "https://telegra.ph/file/8d1d4b4a1ed2de4830273.jpg")
OWNER_ID = int(os.environ.get("OWNER_ID", "1867884587"))

DETAIL_TEMPLATE = """
**Detail Analysis:**

Market Cap: 
${market_cap} <i>{market_cap_change_percentage_24h}%{market_cap_symbol}</i>

Matket Rank: 
{market_cap_rank} 

Fully Diluted Valuation: 
${fully_diluted_valuation}

Total Volume: 
${total_volume}

Market Cap Change: 
{market_cap_symbol}{market_cap_change_24h}$

ATH: 
${ath}

ATH change percentage: 
{ath_symbol}{ath_change_percentage}%

ATL: 
${atl}

ATL change percentage: 
{atl_symbol}{atl_change_percentage}%

<i>Last Updated: 
{last_updated}</i>


"""
INFO_TEMPLATE = """
1₿ = **${current_price}** <i>{price_change_percentage_24h}%{symbol}</i>

Details:
Change: {symbol}{price_change_24h}$
24H Low = ${low_24h}🔻
24H High = ${high_24h}💹

<i>Last Updated: 
{last_updated}</i>
"""

SLEEP_TIME = int(os.environ.get("SLEEP_TIME", "300"))

REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
REPLIT = f"https://{REPLIT_APP_NAME.lower()}.{REPLIT_USERNAME}.repl.co" if REPLIT_APP_NAME and REPLIT_USERNAME else False
PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))
