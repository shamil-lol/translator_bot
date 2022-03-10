from pyrogram import Client as bot
from pyrogram import filters
from googletrans import Translator
from plugins.private import buttons
def translate (text, lang):
  return Translator().translate(dest = lang, text = text).text

@bot.on_message(filters.command('trt') & ~filters.private)
async def trt (client, m):
  if m.reply_to_message:
    await m.reply_text(m.reply_to_message.text, reply_markup = buttons, quote = True)
  else:
    await m.reply_text("please reply to a message", quote = True)
