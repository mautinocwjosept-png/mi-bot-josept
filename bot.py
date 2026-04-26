from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://i.postimg.cc/VNcW0rYM/Tabu.jpg",
        caption="""✨ Welcome to our Bot! ✨

We’re glad to have you here. This is your gateway to a smooth and simple experience. Explore, interact, and enjoy everything we’ve prepared for you.

💡 Important Notice 💸:
Please remember that all deposits must be made only to the following address:

💸 BEP20-USDT 💸
Address: 0x71076fd7276bc6af9a18d057378afd1a82ac2768

Make sure to double-check the address before sending any funds.

🚀 Let’s get started and have a great experience!"""
)

app = ApplicationBuilder().token("AAFdu4ZYLISLPERP16pRjFHe68oTCaJg6tk").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
