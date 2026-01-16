import logging
import time
import pytz
import requests
import threading
import os
import asyncio
import uvloop
from pyrogram import types, Client, filters
from typing import Union, Optional, AsyncGenerator
from .utils import temp
from datetime import date, datetime
from Script import script
from aiohttp import web
from AutoPosterBot.plugins import smdxserver
from config import LOG_CHANNEL, API_ID, API_HASH, BOT_TOKEN, PORT, URL

uvloop.install()

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logging.getLogger('pyrogram').setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

def ping_loop():
    while True:
        try:
            r = requests.get(URL, timeout=10)
            if r.status_code == 200:
                print("✅ MR.X ᴘɪɴɢ sᴜᴄᴄᴇssғᴜʟ")
            else:
                print(f"⚠️ sᴍᴅʙᴏᴛᴢ ᴘɪɴɢ ғᴀɪʟᴇᴅ: {r.status_code}")
        except Exception as e:
            print(f"❌ ᴇxᴄᴇᴘᴛɪᴏɴ ᴅᴜʀɪɴɢ ᴘɪɴɢ: {e}")
        time.sleep(120)

threading.Thread(target=ping_loop, daemon=True).start()

class Bot(Client):
    def __init__(self):
        super().__init__(
            name='Auto_Filter_Bot',
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="AutoPosterBot/plugins")
        )

    async def start(self):
        await super().start()
        temp.START_TIME = time.time()
        temp.BOT = self
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        logger.info(script.LOGO)
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        timex = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, timex))
        
        # 🕸️ Web Support ⚡ #
        app = web.AppRunner(await smdxserver())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        logger.info("Bot Stopped! Bye...")

    async def iter_messages(self: Client, chat_id: Union[int, str], limit: int, offset: int = 0) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1


app = Bot()
app.run()
