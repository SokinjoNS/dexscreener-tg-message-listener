# Dexscreener Telegram Message Listener

The __dexscreener_tg_message_listener.py__ module is part of a Telegram bot application designed to listen for and process messages containing URLs from Dexscreener. It extracts relevant data and forwards is via Telegram messages.

## Features

- __URL Parsing:__ Efficiently identifies and parses Dexscreener URLs in Telegram messages.
- __Data Extraction:__ Extracts trading pair addresses from the parsed URL and retrieves relevant trading data using the Dexscreener API.
- __Telegram Alerts:__ Sends formatted alerts to a specified Telegram chat with the extracted data.

## Prerequisites

- Python 3.6 or newer.
- A Telegram bot token and API credentials (__api_id__ and __api_hash__).
- Access to the Dexscreener API for data extraction.
- The requests library for making HTTP requests to the Dexscreener API.
- The telethon library for interacting with the Telegram API.

## Installation

__1. Clone the Repository:__

```bash
git clone https://your-repository-url.git
cd your-repository-directory
```
__2. Install Dependencies:__

This script requires the requests and telethon libraries. Install them using pip:

```bash
pip install requests telethon
```

__Configure Your Credentials:__

Rename __credentials_telegram.json.example__ to __credentials_telegram.json__ and update it with your Telegram API api_id, api_hash, and bot token, along with any required Dexscreener API keys.

```bash
{
  "api_id": "YOUR_API_ID",
  "api_hash": "YOUR_API_HASH",
  "bot_token": "YOUR_BOT_TOKEN",
  "dextools_api_key": "YOUR_DEXTOOLS_API_KEY" // If needed
}
```

## Usage

To utilize this module within your Telegram bot application, ensure it's imported and integrated with your main bot script, typically tg_message_listener_main.py. The main script should handle incoming messages and delegate to this module when a Dexscreener URL is detected.

## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Support

For issues, questions, or contributions, please open an issue in the GitHub repository.

Feedback and contributions are welcome!

## License

This module is released under the MIT License. See the LICENSE file in the repository for full licensing details.
