import requests
import json
from telegram_alerts import handle_and_send_message

def load_telegram_credentials():
    with open('credentials_telegram.json') as f:
        credentials = json.load(f)
    return credentials

def get_contract_addresses_from_pair_query(query):
    url = f"https://api.dexscreener.com/latest/dex/search?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'pairs' in data and data['pairs']:
            token0_address = data['pairs'][0]['baseToken']['address']
            # Assuming you're only interested in token0_address for the alert
            return token0_address
    return None

def handle_dexscreener_message(message):
    credentials = load_telegram_credentials()
    # Simplifying the extraction of pair_address from the message
    if "dexscreener.com/ethereum/" in message:
        query = message.split("dexscreener.com/ethereum/")[-1]
        token_address = get_contract_addresses_from_pair_query(query)
        if token_address:
            # Adjusting details to match expected structure in telegram_alerts
            details = {
                'token_address': token_address
            }
            # Directing the message correctly using 'response_chat_id'
            handle_and_send_message('dexscreener', details, credentials)
        else:
            print("Failed to fetch token address from Dexscreener URL.")

