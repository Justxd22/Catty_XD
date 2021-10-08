from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update, InlineQueryResultPhoto, InlineQueryResultMpeg4Gif, InlineKeyboardMarkup
import os, time, sys, subprocess, requests, logging, datetime, pytz, json, signal, telegram 
from uuid import uuid4
from random import randint

x = datetime.datetime.utcnow()
i = x + datetime.timedelta(hours=3)
y = i.strftime("%Y-%m-%d_%I:%M%P")
d = i.strftime("%Y-%m-%d")
na = d + ".txt"
print(y)
desexis = False
descr = ""
print("My PID is:", os.getpid())
o = open(na, "a")

app_name = os.getenv("RAILWAY_STATIC_URL", "")
if len(str(app_name)) < 2:
   app_name_heroku = os.getenv("HEROKU_APP_NAME", "")
   if app_name_heroku == "":
      print("please put your app url for webhook in env or disable webhook")
      sys.exit(1)
   else:
      app_name = "https://" app_name_heroku + ".herokuapp.com/"

PORT = int(os.environ.get('PORT', 5000))

token = os.getenv("token", "")
if len(str(token)) < 5: print("please put your token in env"); sys.exit(1)

kb = [[telegram.KeyboardButton('🐈 Kitty'), telegram.KeyboardButton('🥺 Heal me ✨')],
      [telegram.KeyboardButton('🤖 Start the Bot'), telegram.KeyboardButton('⁉️ Help')]]

kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard = True)

def start(update, context):
    update.message.reply_text("""
    HI, I'M CATTY NICE TO MEET YOU
    this bot help smooth your mood remotely
    send /help to list available commands""", reply_markup=kb_markup)
    print("New user !", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title))
    print("New user !", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title), file = o)
    o.flush()

def help(update, context):
    update.message.reply_text(
    """
    HI again
     /help --display this list
     /cat  --Cute surprize
     /heal --No describtion try at your own risk!!
     Go on try something
    """, reply_markup=kb_markup)
    print("USER NEED HELP!", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title))
    print("USER NEED HELP!", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title), file = o)
    o.flush()

def url():
    rse = requests.get(
    'https://api.thecatapi.com/v1/images/search',headers={'x-api-key': 'ff14eeeb-bf85-45c2-985a-087f81b1d69c'})
    js = json.loads(rse.text)
    urlp = js[0]['url']
    dchk = js[0]["breeds"]
    global desexis
    if len(dchk) == 0:
       print("no breeds")
       desexis = False
    else:
       desr = js[0]["breeds"][0]['description']
       if len(desr) == 0:
          print("no des")
       else:
          global descr
          descr = desr
          desexis = True
    print(urlp)
    return urlp


def cat(update, context):
    print("\aHands off new cat!")
    print("new req from ", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title), file = o)
    print("new req from ", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title))
    urlk = url()
    if ".jpg" in urlk or ".png" in urlk or ".jpeg" in urlk:

       if desexis is  True:
          capt = descr
          context.bot.send_photo(chat_id=update.message.chat_id, photo=urlk, caption=capt)
       else:
          context.bot.send_photo(chat_id=update.message.chat_id, photo=urlk)

    elif ".gif" in urlk:

         if desexis is  True:
            capt = descr
            context.bot.send_animation(chat_id=update.message.chat_id, animation=urlk, caption=capt)
         else:
            context.bot.send_animation(chat_id=update.message.chat_id, animation=urlk)
    else:
       print("link error")
       print("link error", urlk , file = o)

    update.message.reply_text(text="powered by @xd2222 PM if u want")
    print("Sent: " + urlk, file=o)
    print("Sent")
    o.flush()

def heal(update, context):
    print("Starting turbo engine ", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title), file = o); o.flush()
    print("Starting turbo engine ", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title))
    for i in range(100):
        urlk = url()
        if ".jpg" in urlk or ".png" in urlk or ".jpeg" in urlk:
            if desexis is  True:
                capt = descr
                context.bot.send_photo(chat_id=update.message.chat_id, photo=urlk, caption=capt)
            else:
                context.bot.send_photo(chat_id=update.message.chat_id, photo=urlk)
        elif ".gif" in urlk:
            if desexis is  True:
                capt = descr
                context.bot.send_animation(chat_id=update.message.chat_id, animation=urlk, caption=capt)
            else:
                context.bot.send_animation(chat_id=update.message.chat_id, animation=urlk)
        else:
            print("link error")
            print("link error", urlk , file = o)

    update.message.reply_text(text="powered by @xd2222 PM if u want", reply_markup=kb_markup)
    print("Sent: " + urlk, file=o)
    print("Sent")
    o.flush()

def listfil(update, context): # for sending log file
    print("List files from ", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title))
    print("List files from ", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title), file = o)
    flsh()
    q = os.listdir()
    r = open("ki.txt", "w+")
    w = json.dump(q, r, indent =2)
    n = r.close()
    e = open("ki.txt", "r")
    z = e.read()
    print(z)
    print(z, file = o.l)
    t = update.message.reply_text(z)

def sendfil(update, context): # secret command for sending log file
    print("Send files to ", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title))
    print("Send files to ", str(update.message.chat.first_name), str(update.message.chat.last_name), str(update.effective_user.username), str(update.message.chat.id), str(update.message.chat.title), file = o)
    clo = o.flush()
    context.bot.send_document(chat_id=update.message.chat_id, document = open(na, "rb"))
    print("file sent s")
    print("file sent s", file = o)
    o.flush()


def inlinequery(update, context):
    print("Inline from ", str(update.effective_user.first_name), str(update.effective_user.last_name), str(update.effective_user.username))
    print("Inline from ", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username), file = o)
    query = update.inline_query.query
    urrl = url()
    print("somone used inline: " + urrl, file = o)

    if ".jpg" in urrl or ".png" in urrl or ".jpeg" in urrl:

       if desexis is True:
          re = [
              InlineQueryResultPhoto(
                  id=uuid4(),
                  photo_url=urrl,
                  thumb_url=urrl,
                  caption = descr
              )
          ]
          update.inline_query.answer(re, cache_time=0)
       else:
          re = [
              InlineQueryResultPhoto(
                  id=uuid4(),
                  photo_url=urrl,
                  thumb_url=urrl
              )
          ]
          update.inline_query.answer(re, cache_time=0)

    elif ".gif" in urrl:

         if desexis is True:
            re = [
                InlineQueryResultMpeg4Gif(
                    id=uuid4(),
                    mpeg4_url=urrl,
                    thumb_url=urrl,
                    caption = descr
                )
            ]
            update.inline_query.answer(re, cache_time=0)

         else:
            re = [
                InlineQueryResultMpeg4Gif(
                    id=uuid4(),
                    mpeg4_url=urrl,
                    thumb_url=urrl
                )
            ]
            update.inline_query.answer(re, cache_time=0)

    else:
       print("link error")
       print("link error", urrl, file = o)
    o.flush()


def thak(update, context):

    ran = randint(0, 1)
    if ran == 1:
       update.message.reply_text("😊 You are welcome")
    else:
       update.message.reply_text("😊 it's my duty")
    print("Thanks from ", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username), file = o)
    print("Thanks from ", str(update.effective_user.first_name), str(update.effective_user.last_name) ,str(update.effective_user.username))
    o.flush()

def main():

    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text('🤖 Start the Bot'), start))
    dp.add_handler(MessageHandler(Filters.text('🥺 Heal me ✨'), heal))
    dp.add_handler(MessageHandler(Filters.text('🐈 Kitty'), cat))
    dp.add_handler(MessageHandler(Filters.text('⁉️ Help'), help))
    dp.add_handler(MessageHandler(Filters.text('thanks'), thak))
    dp.add_handler(MessageHandler(Filters.text('thank you'), thak))
    dp.add_handler(MessageHandler(Filters.text('cute'), cat))
    dp.add_handler(MessageHandler(Filters.text('Thanks'), thak))
    dp.add_handler(MessageHandler(Filters.text('Thank you'), thak))
    dp.add_handler(MessageHandler(Filters.text('Cute'), cat))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('heal', heal))
    dp.add_handler(CommandHandler('cat', cat))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('secp12', listfil))
    dp.add_handler(CommandHandler('secp13', sendfil))
    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, cat))
    dp.add_handler(MessageHandler(Filters.photo, cat))
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=token)  # comment for local testing
    updater.bot.setWebhook(app_name + token)  # comment for local testing
    #updater.start_polling() # uncomment for local testing
    updater.idle()
    o.flush()
    print ("ok")

main()
