from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (
    Updater, 
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    Filters
)

MANBA = 1
SINOV = 2

BTN_USER, BTN_RESURS, BTN_ANALYSIS, BTN_RESULT, BTN_SELF = ('👤 Foydalanuvchi', '📚 Manbalar', '🧪 Sinov', '📊 Mening Natijalarim', '📞 Biz bilan aloqa')

main_buttons = ReplyKeyboardMarkup([
        [BTN_USER, BTN_RESURS], [BTN_ANALYSIS, BTN_RESULT], [BTN_SELF]
    ], resize_keyboard = True)

def start(update, context):
    user = update.message.from_user
    buttons = [
        [
            InlineKeyboardButton('Matem', callback_data = 'fan1'),
            InlineKeyboardButton('Fizika', callback_data = 'fan2')
        ]
    ]

    update.message.reply_text('Assalomu Aleykum {} \n<b>Sizga qaysi fan bo`yicha ma`lumot beraylik!</b>'.
        format(user.first_name),
        reply_markup = InlineKeyboardMarkup(buttons),
        parse_mode = "HTML")
    return SINOV

def self_user():
    update.message.reply_text('Foydalanuvchi bosildi')

def self_manba():
    update.message.reply_text('Manbalar bosildi')

def self_sinov():
    update.message.reply_text('Sinov bosildi')

def self_natija():
    update.message.reply_text('Meningnatijalaim bosildi')

def self_Aloqa():
    update.message.reply_text('aloqa bosildi')


def zaproslar(update, context):

    query = update.callback_query
    query.message.delete()
    query.message.reply_text('<i>Tegishli bo`limni tanlang:</i> 👇',
        reply_markup = main_buttons,
        parse_mode = "HTML")
    return MANBA

def asosiy():
    #updater - yangilanuvchi
    updater = Updater('1880690891:AAFkFv7O1oGUj3KqyyMmgDcdwmB2-zJ3EGU', use_context = True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            SINOV: [CallbackQueryHandler(zaproslar)],
            MANBA: [
                MessageHandler(Filters.regex('^('+BTN_USER+')$'), self_user),
                MessageHandler(Filters.regex('^('+BTN_USER+')$'), self_manba),
                MessageHandler(Filters.regex('^('+BTN_USER+')$'), self_sinov),
                MessageHandler(Filters.regex('^('+BTN_USER+')$'), self_natija),
                MessageHandler(Filters.regex('^('+BTN_USER+')$'), self_Aloqa)
            ]
        },
        fallbacks = [CommandHandler('start', start)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

asosiy()






'''
def start(update, context):
    try:
        contact_keyboard = telegram.KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
        custom_keyboard = [
            [
                contact_keyboard
            ]
        ]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True)
        
        update.message.reply_text(
                text = '<b>Botdan foylanishingiz uchun iltimos</b>\n<i>Telefon raqam</i>ingizni yuboring: 👇', 
                reply_markup = reply_markup,
                parse_mode = "HTML"
                )
    except Exception as e:
        print(str(e))
'''
