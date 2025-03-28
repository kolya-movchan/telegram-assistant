import os
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your Telegram API credentials from the .env file
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")
auto_reply = os.getenv("AUTO_REPLY")

# Initialize the Telegram client
client = TelegramClient("session_name", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()
    if not sender.bot:  # Exclude bot messages
        print(f"Received a message from {sender.username or sender.phone}: {event.message.message}")
        # Wait for 2 seconds before replying
        await asyncio.sleep(2)
        await event.reply(auto_reply)

client.start(phone=phone_number)
print("Auto-reply bot is running...")
client.run_until_disconnected()
