from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from googletrans import Translator

@bot.on_inline_query()
async def inline_query (client, m):
    text = m.query
    if m.chat_type == "sender":
      await m.answer(results = [], switch_pm_text = "You Can't Use Me In My Chat, Please Switch To Another Chat", switch_pm_parameter = "enc-own_chat")
    else:
      try:
        en = Translator().translate(dest = "en", text = text).text
        am = Translator().translate(dest = "am", text = text).text
        ar = Translator().translate(dest = "ar", text = text).text
        es = Translator().translate(dest = "es", text = text).text
        fr = Translator().translate(dest = "fr", text = text).text
        tr = Translator().translate(dest = "tr", text = text).text
      except Exception:
        pass
      try:
        await m.answer(results = [
        InlineQueryResultArticle(
        "ENGLISH",
        InputTextMessageContent(en)
        ),
        InlineQueryResultArticle(
        "AMHARIC",
        InputTextMessageContent(am)
        ),
        InlineQueryResultArticle(
        "ARABIC",
        InputTextMessageContent(ar)
        ),
        InlineQueryResultArticle(
        "SPANISH",
        InputTextMessageContent(es)
        ),
        InlineQueryResultArticle(
        "FRENCH",
        InputTextMessageContent(fr)
        ),
        InlineQueryResultArticle(
        "TURKISH",
        InputTextMessageContent(tr)
        )
        ])
      except Exception as e:
        pass
