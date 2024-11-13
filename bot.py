from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Токен вашего бота (замените на ваш токен)
BOT_TOKEN = "7724793156:AAHXBbg5VYnCht7dY4g6XYPczXR5xeGKj3U" 

async def start(update: Update, context):
    await update.message.reply_text('Привет! Ща буду чудить. ваш бебра ботт.')

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    app.run_polling()

if __name__ == '__main__':
    main()
