from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("Press the button to send a message to the bot owner:")

def main():
    updater = Updater("5382964532:AAH8GdCkXCv4zsc5SkH0LY-dnDUobGHBJBg", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

main()