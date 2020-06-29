import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
##enable logging
logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)
TOKEN='token key'
##create updater
def start(bot,update):
    print(update)
    author=update.message.from_user.first_name
    reply="Hi! {}".format(author)
    bot.send_message(chat_id=update.message.chat_id,text=reply)
def _help(bot,update):
    help_text="HEY! Lets Go Vroom for help"
    bot.send_message(chat_id=update.message.chat_id,text=help_text)
    
def echo_text(bot,update):
    reply=update.message.text
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def echo_sticker(bot,update):
    bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)

def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update,update.error)
    
    
    
def main():
    updater=Updater(TOKEN)
    ## dispatecher object
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)
    updater.start_polling()
    logger.info("Start polling.....")
    updater.idle()

if __name__=="__main__":
    main()
