from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.deeplink import deep_links
buttons = InlineKeyboardMarkup([
[InlineKeyboardButton(text = "USE INLINE MODE", switch_inline_query_current_chat = "")],
[InlineKeyboardButton(text = "JOIN OUR GROUP", url = "https://t.me/Ethiopians_project"),
InlineKeyboardButton(text = "CONTACT OWNER", url = "https://t.me/shamil01_bot")]
])
@bot.on_message(filters.private & filters.command('start'))
async def start (client, m):
  start_message = f"hello {m.chat.first_name},\nWelcome to translator bot"
  dl = m.text.replace("/start ", "")
  if dl == m.text:
    await m.reply_text(start_message, reply_markup = buttons)
  elif dl in deep_links:
    await m.reply_text(deep_links[dl])
  else:
    await m.reply_text(start_message, reply_markup = buttons)
