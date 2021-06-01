from telebot import *
from telebot import types
import telegram, time, requests
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

bot1 = TeleBot("1540433300:AAFhC6LYbtzGi3qAp6_Ctd7Qn0zm10WFOtA")


@bot1.message_handler(commands=["calendar", "today"])
def calendar(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot1.send_message(
        m.chat.id,
        f"Select <b>Today</b> if joined today or Select <b>{LSTEP[step]}</b>",
        reply_markup=calendar,
        parse_mode="html",
    )


@bot1.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot1.edit_message_text(
            f"Select {LSTEP[step]}",
            c.message.chat.id,
            c.message.message_id,
            reply_markup=key,
        )
    elif result:
        bot1.edit_message_text(
            f"You selected {result}", c.message.chat.id, c.message.message_id
        )
        print(result)


@bot1.message_handler(commands=["start", "help"])
def start(m):
    chat_id = m.chat.id
    fn = m.chat.first_name
    ln = m.chat.last_name
    username = m.chat.username

    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("👤 New User Registration", callback_data="1")
    )
    keyboard.row(types.InlineKeyboardButton("🚀 Signals", callback_data="2"))
    bot1.send_chat_action(chat_id=chat_id, action="typing")
    bot1.send_message(
        chat_id,
        f"Hello {['@' if username else fn if fn else ln][0]}<b>{username}</b> 😊\n\nI'm TMS's ULTRON 🤖\n\nWelcome to 𝑻𝒓𝒖𝒔𝒕𝒎𝒚𝒔𝒕𝒐𝒄𝒌'𝒔 𝑽𝑰𝑷 𝑪𝑯𝑨𝑻\n\nMy job is to handle \n\n➕ New Member Registrations\n\n🚀 Signal Management",
        parse_mode="html",
        reply_markup=keyboard,
    )


@bot1.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    normal_messages = [
        "hi",
        "hello",
        "hey",
        "help",
        "how are you",
        "what's up",
        "hii",
        "helloooo",
    ]
    if (
        text.lower() == normal_messages[0]
        or text.lower() == normal_messages[1]
        or text.lower() == normal_messages[2]
        or text.lower() == normal_messages[3]
        or text.lower() == normal_messages[4]
        or text.lower() == normal_messages[5]
        or text.lower() == normal_messages[6]
    ):
        id = message.chat.id
        fn = message.chat.first_name
        ln = message.chat.last_name
        username = message.chat.username

        bot1.send_chat_action(chat_id=id, action="typing")

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton("👤 New User Registration", callback_data="1")
        )
        keyboard.add(types.InlineKeyboardButton("🚀 Signals", callback_data="2"))
        bot1.reply_to(
            message,
            f"Hello {['@' if username else fn if fn else ln][0]}<b>{username}</b> 😊\n\nI'm TMS's ULTRON 🤖\n\nWelcome to 𝑻𝒓𝒖𝒔𝒕𝒎𝒚𝒔𝒕𝒐𝒄𝒌'𝒔 𝑽𝑰𝑷 𝑪𝑯𝑨𝑻\n\nMy job is to handle \n\n➕ New Member Registrations\n\n🚀 Signal Management",
            parse_mode="html",
            reply_markup=keyboard,
        )
    # else:
    #     bot1.send_chat_action(chat_id=message.chat.id, action="typing")
    #     bot1.reply_to(
    #         message,
    #         "Sorry I can't understand 😕\n\nYou can access me with the below Commands \n\n/start or /help 😊",
    #     )


def NameHandler(message):
    try:
        chat_id = message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            types.InlineKeyboardButton("Yes", callback_data="name-y"),
            types.InlineKeyboardButton("No", callback_data="name-n"),
        )
        msg = bot1.send_message(
            chat_id=chat_id, text=f"Your Name {message.text}", reply_markup=keyboard
        )
    except Exception as e:
        bot1.reply_to(message, "oooops")


def InstagramHandler(message):
    try:
        chat_id = message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            types.InlineKeyboardButton("Yes", callback_data="insta-y"),
            types.InlineKeyboardButton("No", callback_data="insta-n"),
        )
        msg = bot1.send_message(
            chat_id=chat_id,
            text=f"Your Instagram Handle {message.text}",
            reply_markup=keyboard,
        )
    except Exception as e:
        bot1.reply_to(message, "oooops")


def MobileNumberHandler(message):
    try:
        chat_id = message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            types.InlineKeyboardButton("Yes", callback_data="mn-y"),
            types.InlineKeyboardButton("No", callback_data="mn-n"),
        )
        msg = bot1.send_message(
            chat_id=chat_id,
            text=f"Your Mobile Number {message.text}",
            reply_markup=keyboard,
        )
    except Exception as e:
        bot1.reply_to(message, "oooops")


@bot1.callback_query_handler(func=lambda call: True)
def button1(m):
    query = m
    chat_id = m.message.chat.id
    first_name = m.message.chat.first_name
    last_name = m.message.chat.last_name

    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choice = query.data

    if choice == "1":
        try:
            bot1.send_chat_action(chat_id=chat_id, action="typing")
            namereq = bot1.send_message(
                chat_id=chat_id,
                text="Please Enter your name",
                parse_mode="html",
            )
            bot1.register_next_step_handler(namereq, NameHandler)

        except telegram.error.BadRequest as blocked:
            if "Forbidden: bot1 was blocked by the user" in blocked.message:
                bot1.send_chat_action(chat_id=chat_id, action="typing")
                bot1.send_message(chat_id=chat_id, text="Blocked")

    elif choice == "2":
        try:
            bot1.send_chat_action(chat_id=chat_id, action="typing")

            keyboard = types.ReplyKeyboardMarkup(
                row_width=1, resize_keyboard=True, one_time_keyboard=True
            )
            keyboard.row(
                types.KeyboardButton("/today"), types.KeyboardButton("/calendar")
            )

            bot1.send_message(
                chat_id=chat_id,
                text="Select <b>today</b> to see today's signal or select <b>calendar</b> to select a date",
                parse_mode="html",
                reply_markup=keyboard,
            )
        except telegram.error.BadRequest as blocked:
            if "Forbidden: bot1 was blocked by the user" in blocked.message:
                bot1.send_chat_action(chat_id=chat_id, action="typing")
                bot1.send_message(chat_id=chat_id, text="Blocked")
    elif choice == "name-y":
        try:
            bot1.send_chat_action(chat_id=chat_id, action="typing")
            instareq = bot1.send_message(
                chat_id=chat_id,
                text="Please Enter your Instagram Handle with <b>@</b>",
                parse_mode="html",
            )
            bot1.register_next_step_handler(instareq, InstagramHandler)

        except telegram.error.BadRequest as blocked:
            if "Forbidden: bot1 was blocked by the user" in blocked.message:
                bot1.send_chat_action(chat_id=chat_id, action="typing")
                bot1.send_message(chat_id=chat_id, text="Blocked")

    elif choice == "insta-y":
        try:
            bot1.send_chat_action(chat_id=chat_id, action="typing")
            mobilereq = bot1.send_message(
                chat_id=chat_id,
                text="Please Enter your <b>mobile number</b>",
                parse_mode="html",
            )
            bot1.register_next_step_handler(mobilereq, MobileNumberHandler)

        except telegram.error.BadRequest as blocked:
            if "Forbidden: bot1 was blocked by the user" in blocked.message:
                bot1.send_chat_action(chat_id=chat_id, action="typing")
                bot1.send_message(chat_id=chat_id, text="Blocked")

    elif choice == "mn-y":
        try:
            bot1.send_chat_action(chat_id=chat_id, action="typing")
            datereq = bot1.send_message(
                chat_id=chat_id,
                text="Please Selecct the date of joining",
                parse_mode="html",
            )
            bot1.register_next_step_handler(datereq, calendar)

        except telegram.error.BadRequest as blocked:
            if "Forbidden: bot1 was blocked by the user" in blocked.message:
                bot1.send_chat_action(chat_id=chat_id, action="typing")
                bot1.send_message(chat_id=chat_id, text="Blocked")


while True:
    try:
        bot1.polling(none_stop=True,timeout=100000)
    except Exception:
        time.sleep(2)