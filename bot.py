from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8902798363:AAFCanVj2Eyipw0V0_ksXi0mJiAgGRyaczg"

GRUPOS = [
    -5567814912,
    -1004341665928
]

async def enviar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Solo acepta mensajes privados
    if update.effective_chat.type != "private":
        return

    for grupo in GRUPOS:

        if update.message.photo:
            await context.bot.send_photo(
                chat_id=grupo,
                photo=update.message.photo[-1].file_id,
                caption=update.message.caption
            )

        elif update.message.video:
            await context.bot.send_video(
                chat_id=grupo,
                video=update.message.video.file_id,
                caption=update.message.caption
            )

        elif update.message.document:
            await context.bot.send_document(
                chat_id=grupo,
                document=update.message.document.file_id,
                caption=update.message.caption
            )

        elif update.message.audio:
            await context.bot.send_audio(
                chat_id=grupo,
                audio=update.message.audio.file_id,
                caption=update.message.caption
            )

        elif update.message.voice:
            await context.bot.send_voice(
                chat_id=grupo,
                voice=update.message.voice.file_id
            )

        elif update.message.animation:
            await context.bot.send_animation(
                chat_id=grupo,
                animation=update.message.animation.file_id,
                caption=update.message.caption
            )

        elif update.message.sticker:
            await context.bot.send_sticker(
                chat_id=grupo,
                sticker=update.message.sticker.file_id
            )

        elif update.message.text:
            await context.bot.send_message(
                chat_id=grupo,
                text=update.message.text
            )

    await update.message.reply_text("✅ Mensaje enviado a los grupos.")

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL & ~filters.COMMAND, enviar)
)

print("Bot listo...")
app.run_polling()
