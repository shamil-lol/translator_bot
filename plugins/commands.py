from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = InlineKeyboardMarkup([
[InlineKeyboardButton(text = "USE INLINE MODE", switch_inline_query_current_chat = "")],
[InlineKeyboardButton(text = "JOIN OUR GROUP", url = "https://t.me/Ethiopians_project"),
InlineKeyboardButton(text = "CONTACT OWNER", url = "https://t.me/shamil01_bot")]
])
@bot.on_message(filters.private & filters.command('start'))
async def start (client, m):
  await m.reply_text(f"hello {m.chat.first_name},\nWelcome to translator bot", reply_markup = buttons)
