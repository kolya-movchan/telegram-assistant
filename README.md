# Telegram Auto-Reply Bot

This is a simple Telegram bot that automatically replies to incoming messages.

## Prerequisites

- Python 3.7 or higher
- Telegram API credentials (API ID and API Hash)

## Setup Instructions

1. Clone this repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate  # On macOS/Linux
# or
myenv\Scripts\activate  # On Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
(OR) pip install telethon python-dotenv
```

4. Create a `.env` file in the root directory with the following variables:

```
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=your_phone_number
AUTO_REPLY=your_auto_reply_message
```

To get your API credentials:

1. Go to https://my.telegram.org/auth
2. Log in with your phone number
3. Go to 'API development tools'
4. Create a new application
5. Copy the API ID and API Hash

## Running the Bot

1. Make sure your virtual environment is activated
2. Run the bot:

```bash
python3 index.py
```

3. On first run, you'll need to authenticate with your Telegram account:
   - Enter your phone number when prompted
   - Enter the verification code sent to your Telegram account

The bot will now automatically reply to any incoming messages with the message specified in the `AUTO_REPLY` environment variable.

## Notes

- The bot will wait for 2 seconds before replying to messages
- Bot messages are excluded from auto-replies
- Make sure to keep your `.env` file secure and never commit it to version control
