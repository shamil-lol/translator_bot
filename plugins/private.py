from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttons = InlineKeyboardMarkup([
[InlineKeyboardButton(text = "USE INLINE MODE", switch_inline_query_current_chat = "")],
[InlineKeyboardButton(text = "ENGLISH", callback_data = "en"),
InlineKeyboardButton(text = "AMHARIC", callback_data = "am")],
[InlineKeyboardButton(text = "ARABIC", callback_data = "ar"),
InlineKeyboardButton(text = "SPANISH", callback_data = "es")],
[InlineKeyboardButton(text = "FRENCH", callback_data = "fr"),
InlineKeyboardButton(text = "TURKISH", callback_data = "tr")]
])

@bot.on_message(filters.private & ~filters.command('start'))
async def msg (client, m):
  await m.reply_text(m.text, reply_markup = buttons, quote = True)
