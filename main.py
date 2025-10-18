import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ня~ я Марилла! (ฅ•ω•ฅ)♡")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "привет" in text:
        await update.message.reply_text("Приветик! ☆*:.｡.o(≧▽≦)o.｡.:*☆")
    else:
        await update.message.reply_text("Мрр~ я не совсем поняла, но звучит мило! (⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)")

app = ApplicationBuilder().token(7845911101:AAFexramcay2zfbKarBkub0GQ5YGifb57C4).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

if __name__ == "__main__":
    app.run_polling()
