from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from googletrans import Translator

updater = Updater('2141947477:AAE0unZyWXR8SaCNingJ3xnYtuXlRLew3Lk',use_context = True )

def start(updater,context):
 updater.message.reply_text('Salom, Men Tarjimon botman!')
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator = Translator()
 translation = translator.translate(usr_msg,dest='uz') 
 updater.message.reply_text(translation.text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
