from re import U
from telegram import *
from telegram.ext import *
from telegram import TelegramError
from telebot import *
from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP


bot = Bot("1849417198:AAHR2-o8d20OJ4sVzBMuHbcj8_ZEzHCpMZs")
updater = Updater("1849417198:AAHR2-o8d20OJ4sVzBMuHbcj8_ZEzHCpMZs", use_context=True)

dispatcher = updater.dispatcher


def calendar(update: Update, context: CallbackContext):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(
        update.message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar
    )


def cal(update: Update, context: CallbackContext):
    result, key, step = DetailedTelegramCalendar().process(update.callback_query.data)
    if not result and key:
        bot.edit_message_text(
            f"Select {LSTEP[step]}",
            update._effective_message.chat.id,
            update._effective_message.message_id,
            reply_markup=key,
        )
    elif result:
        bot.edit_message_text(
            f"You selected {result}",
            update._effective_message.chat.id,
            update._effective_message.message_id,
        )
        print(result.strftime("%m-%d-%y"))


dispatcher.add_handler(CommandHandler("calendar", calendar))
dispatcher.add_handler(CallbackQueryHandler(cal))

updater.start_polling()