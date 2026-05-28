
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from configs.telegram_config import get_tgbio_text
from pyrogram import *
from dotenv import load_dotenv
import asyncio

load_dotenv()

app = Client("AwesomeSetup", api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"))

# @app.on_message(filters.private)
# async def hello(client, message):
#     await message.reply("hi, this is auto message")

async def update_bio():
    while True:
        bio = await get_tgbio_text()
        await app.update_profile(bio=bio)
        print(f"bio in telegram has been updated on {bio}")
        await asyncio.sleep(30)

async def main_tg():
    async with app:
        asyncio.create_task(update_bio())
        await idle() 

# if __name__ == "__main__":
#     asyncio.run(main_tg())