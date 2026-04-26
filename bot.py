from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://i.imgur.com/yKMIKbA.jpeg",
        caption="Hola 👋 Bienvenido"
    )

app = ApplicationBuilder().token("8044397547:AAHC3MHLePxuCYsonnZEaJcvpjthheGIsV4").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
