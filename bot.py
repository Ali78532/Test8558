from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "ضع_التوكن_هنا"

async def start(update: Update, context):
    await update.message.reply_text("مرحبًا! أنا البوت الخاص بك. أرسل لي صورة.")

async def handle_photo(update: Update, context):
    user_id = update.message.from_user.id
    photo = update.message.photo[-1].file_id
    await context.bot.send_photo(chat_id=user_id, photo=photo, caption="تم استلام الصورة!")

async def handle_text(update: Update, context):
    await update.message.reply_text("البوت لا يدعم النصوص. يرجى إرسال صورة فقط.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT, handle_text))
    print("البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()