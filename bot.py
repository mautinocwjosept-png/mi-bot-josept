from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

usuarios = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    if user_id not in usuarios:
        usuarios.add(user_id)

        await update.message.reply_photo(
            photo="https://i.imgur.com/tuimagen.jpg",
            caption=f"Hola {user.first_name} 👋 Bienvenido"
        )
    else:
        await update.message.reply_text(f"Hola de nuevo {user.first_name}")

app = ApplicationBuilder().token("8044397547:AAHC3MHLePxuCYsonnZ EaJcvpjthheGIsV4").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
