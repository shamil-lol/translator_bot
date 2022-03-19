from pyrogram import Client as bot
from pyrogram import filters
from utils.deeplink import docs

@bot.on_message(filters.private & filters.command('api'))
async api_(client, m):
  await m.reply_text(docs)
