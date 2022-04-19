from pyrogram import Client, filters
import logging
from os import getenv as env
logging.basicConfig(level=logging.INFO)
bot = Client(
  api_id = env("API_ID"),
  api_hash = env("API_HASH"),
  bot_token = env("BOT_TOKEN"),
  session_name = "trt",
  plugins = { "root": "plugins" }
  )
bot.run()
