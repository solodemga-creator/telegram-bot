from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN ="8902798363:AAGtFLpdcY_hJu7p19daq-nHKafBs3TdTBQ"
GRUPOS = [
    -5507814912,
    -1004341665928
]

async def enviar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Solo acepta mensajes privados
    if update.effective_chat.type == "private":
        for grupo in GRUPOS:
            await context.bot.send_message(
                chat_id=grupo,
                text=update.message.text
            )

        await update.message.reply_text("✅ Mensaje enviado a los grupos.")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, enviar))

print("Bot listo...")
app.run_polling()