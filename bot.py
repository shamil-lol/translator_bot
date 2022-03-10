from pyrogram import Client, filters
import logging
logging.basicConfig(level=logging.INFO)
bot = Client(
  "trt",
  config_file = "config.ini"
  )
bot.run()
