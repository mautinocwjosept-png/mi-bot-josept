from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://i.postimg.cc/VNcW0rYM/Tabu.jpg",
        caption="Hola 👋 Bienvenido"
    )

app = ApplicationBuilder().token("8044397547:AAF9b7AHR-GNOsJJfPFvN4u7HDlaOg_295o").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
