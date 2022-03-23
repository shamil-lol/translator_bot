from pyrogram import Client as bot
from pyrogram import filters
from googletrans import Translator

def translate (text, lang):
  return Translator().translate(dest = lang, text = text).text

available_langs = ["en", "am", "ar", "es", "ml",  "fr", "tr"]
@bot.on_callback_query()
async def callback_query (client, m):
  try:
    if m.message.text == translate(m.message.text, m.data):
      await m.answer(f"{m.message.text} is {m.message.text}")
    elif m.data in available_langs:
      await m.reply_text(f"{m.message.text}   →   {translate(m.message.text, m.data)}")
    else:
      await m.answer("not availabe")
  except Exception as e:
    await m.answer(f"{e}")
