from telegram import *
from telegram.ext import *
from telegram import TelegramError
import datetime
import time

# my_id = 1243113998
# tms = 879137704



bot = Bot("1849417198:AAHR2-o8d20OJ4sVzBMuHbcj8_ZEzHCpMZs")
updater = Updater("1849417198:AAHR2-o8d20OJ4sVzBMuHbcj8_ZEzHCpMZs", use_context=True)

dispatcher = updater.dispatcher


# chat.id sends in group whit from_user.id send [private]


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = update._effective_user.id

    # print(chat_id)

    first_name = update._effective_user.first_name
    last_name = update._effective_user.last_name
    username = update._effective_user.username
    query.answer()

    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choice = query.data

    # Now u can define what choice ("callback_data") do what like this:
    if choice == "1":
        try:
            bot.send_message(
                chat_id=chat_id,
                text="<i>TMS PROFILE</i>\n\n👤 Your Name: <b>{}</b>\n\n📅 Date Joined: <b>{}</b>\n\n✅ Your Instagram: <b>{}</b>\n\n💰 Your Package: <b>{}</b>\n\n".format(
                    str([first_name if first_name else last_name][0])
                    + " "
                    + str([last_name if last_name else ""][0]),
                    "Will be updated soon",
                    "Will be updated soon",
                    "Will be updated soon",
                ),
                parse_mode=ParseMode.HTML,
            )
        except TelegramError as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )
    elif choice == "2":
        try:
            bot.send_message(
                chat_id=chat_id,
                text="🔔 TMS RULES\n\n✨Please be respectful to everyone in the chat and follow the guidelines set by the chat admin and co-admin(s).\n\n✨Anyone violating group guidelines in group will be kicked immediately.\n\n✨Chat admin and co-admin(s) have the right to kick out potential troublemakers to keep their chat safe. Please be respectful toward their decision.\n\n✨Please be aware this is the internet and be more careful of the content you share online. Do not share your private information.\n\n✨No spamming - this also includes chain messages.\n\n✨No coin begging and advertising.",
            )
        except TelegramError as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )
    elif choice == "3":
        try:
            keyboard = [
                [InlineKeyboardButton("$149.99/Month", callback_data="one_m")],
                [InlineKeyboardButton("$299.99/3 Months", callback_data="three_m")],
                [InlineKeyboardButton("$499.99/6 Months", callback_data="six_m")],
                [InlineKeyboardButton("$999.99/ Year", callback_data="one_y")],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            bot.send_animation(
                chat_id,
                caption="""🎁 TMS PACKAGES

ADD ONE FULL <b>FREE MONTH</b> TO THE FOLLOWING VIP CHAT RATES:
<b>
•  Monthly Rates - <i>$149.99</i>
•  3 Month Rate  - <i>$299.99</i>
•  6 Month Rate. - <i>$499.99</i>
•  Yearly Rates    - <i>$999.99</i>
</b>
💳 Payment Mode: <b>(PayPal, Zelle, Venmo)</b>

GET OFF THE SIDELINES AND RIDE OUR SIGNALS EVERY DAY 🚂🚂💸""",
                parse_mode=ParseMode.HTML,
                animation="https://media.giphy.com/media/fULcqyLb74wqHdd1gW/giphy.gif",
            )
        #             bot.send_message(
        #                 chat_id,
        #                 text="""🎁 TMS PACKAGES

        # ADD ONE FULL <b>FREE MONTH</b> TO THE FOLLOWING VIP CHAT RATES:
        # <b>
        # •  Monthly Rates - <i>$149.99</i>
        # •  3 Month Rate  - <i>$299.99</i>
        # •  6 Month Rate. - <i>$499.99</i>
        # •  Yearly Rates    - <i>$999.99</i>
        # </b>
        # 💳 Payment Mode: <b>(PayPal, Zelle, Venmo)</b>

        # GET OFF THE SIDELINES AND RIDE OUR SIGNALS EVERY DAY 🚂🚂💸""",
        #                 parse_mode=ParseMode.HTML,
        #             )
        except Exception as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )
    elif choice == "4":
        try:
            bot.send_message(
                chat_id=chat_id,
                text="""This is our disclaimer if you have not already received this. 👇

⚠ DISCLAIMER!

• By joining and/or participating in the TrustMyStocks chat room and/or VIP signal chat you hereby understand, consent and agree that you are solely responsible for any and all investment related decisions, strategies and actions that you choose to execute.  TrustMyStocks is not an investment, legal, tax, or financial advisor or a broker-dealer.  We are not licensed or registered stock brokers or investment advisors nor do we in any manner hold ourselves out as investment advisors or securities experts.  Alerts, texts, messages and any other forms  of communication are strictly for entertainment, educational and informational purposes and we are not responsible for any gains or losses incurred as a result of you trading in securities.  You are responsible for your own independent research and due diligence. We highly recommend you consult with licensed experts and always remember there are many inherent risks involved in trading, swing trading, and any buying / selling of securities.  We are not liable for the accuracy or reliability of any information that is provided.  We are offering our personal opinions and nothing more. We are not required to refrain or partake in any buying or selling of any stock, security, commodity or fund that is in any manner discussed on any TrustMyStocks platform.  We will refrain or invest in any given stock, security, commodity or fund at our own personal discretion and without any prior or subsequent notice to you at any point in time or on any platform. 
                
• By accepting these “terms and conditions” you hereby disclaim, release and waive any and all liability, claims, losses or damages directly or indirectly related to any item posted on any TrustMyStocks platform including but not limited to the chat room and VIP signal chat and no fiduciary relationship or duty exists between you and TrustMyStocks.  If you do not fully agree and consent to these “terms and conditions” then do not join or in any manner participate in the chat room or VIP signal chat. 

• By paying the fee to join the VIP signal chat you are acknowledging that you have read the disclaimer and consent to its terms and conditions.

• Please provide Instagram username to @trustmystocks 🚀🚀

• If you don’t send us your Instagram username  for confirmation you will be REMOVED!

• If you did already then you are good!""",
            )
        except Exception as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )
    elif choice == "one_m":
        try:
            bot.send_message(
                chat_id=chat_id,
                text="Thank you for choosing the package. We've sent your choice to the admin and he'll be getting back to you within today. Cheers!!! 🍴",
            )
            bot.send_message(
                chat_id=chat_id,
                text="Package Selection Alert 🦺\n\nUsername : {}\n\nSelected Package : 1 Month - $149".format(
                    username
                ),
            )
        except TelegramError as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )
    elif choice == "three_m":
        try:
            bot.send_message(
                chat_id=chat_id,
                text="Thank you for choosing the package. We've sent your choice to the admin and he'll be getting back to you within today. Cheers!!! 🍴",
            )
            bot.send_message(
                chat_id=chat_id,
                text="Package Selection Alert 🦺\n\nUsername : {}\n\nSelected Package : 3 Months - $299".format(
                    username
                ),
            )
        except TelegramError as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )
    elif choice == "six_m":
        try:
            bot.send_message(
                chat_id=chat_id,
                text="Thank you for choosing the package. We've sent your choice to the admin and he'll be getting back to you within today. Cheers!!! 🍴",
            )
            bot.send_message(
                chat_id=chat_id,
                text="Package Selection Alert 🦺\n\nUsername : {}\n\nSelected Package : 6 Months - $499".format(
                    username
                ),
            )
        except TelegramError as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )
    elif choice == "one_y":
        try:
            bot.send_message(
                chat_id=chat_id,
                text="Thank you for choosing the package. We've sent your choice to the admin and he'll be getting back to you within today. Cheers!!! 🍴",
            )
            bot.send_message(
                chat_id=chat_id,
                text="Package Selection Alert 🦺\n\nUsername : {}\n\nSelected Package : 1 Year - $999".format(
                    username
                ),
            )
        except TelegramError as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )


def packages(update: Update, context: CallbackContext):
    chat_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username

    try:
        keyboard = [
            [InlineKeyboardButton("$149.99/Month", callback_data="one_m")],
            [InlineKeyboardButton("$299.99/3 Months", callback_data="three_m")],
            [InlineKeyboardButton("$499.99/6 Months", callback_data="six_m")],
            [InlineKeyboardButton("$999.99/ Year", callback_data="one_y")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_animation(
            chat_id,
            caption="""🎁 TMS PACKAGES

ADD ONE FULL <b>FREE MONTH</b> TO THE FOLLOWING VIP CHAT RATES:
<b>
•  Monthly Rates - <i>$149.99</i>
•  3 Month Rate  - <i>$299.99</i>
•  6 Month Rate. - <i>$499.99</i>
•  Yearly Rates    - <i>$999.99</i>
</b>
💳 Payment Mode: <b>(PayPal, Zelle, Venmo)</b>

GET OFF THE SIDELINES AND RIDE OUR SIGNALS EVERY DAY 🚂🚂💸""",
            parse_mode=ParseMode.HTML,
            animation="https://media.giphy.com/media/fULcqyLb74wqHdd1gW/giphy.gif",
        )
        #             bot.send_message(
        #                 chat_id,
        #                 text="""🎁 TMS PACKAGES

        # ADD ONE FULL <b>FREE MONTH</b> TO THE FOLLOWING VIP CHAT RATES:
        # <b>
        # •  Monthly Rates - <i>$149.99</i>
        # •  3 Month Rate  - <i>$299.99</i>
        # •  6 Month Rate. - <i>$499.99</i>
        # •  Yearly Rates    - <i>$999.99</i>
        # </b>
        # 💳 Payment Mode: <b>(PayPal, Zelle, Venmo)</b>

        # GET OFF THE SIDELINES AND RIDE OUR SIGNALS EVERY DAY 🚂🚂💸""",
        #                 parse_mode=ParseMode.HTML,
        #             )
    except Exception as e:
        print(e)
        if e.message == "Forbidden: bot was blocked by the user":
            keyboard = [
                [
                    InlineKeyboardButton(
                        "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                    ),
                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_text(
                text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                reply_markup=reply_markup,
            )
        else:
            update._effective_message.reply_text(
                text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
            )


def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username

    try:
        keyboard = [
            [InlineKeyboardButton("👤About Me", callback_data="1")],
            [InlineKeyboardButton("📜Rules", callback_data="2")],
            [InlineKeyboardButton("🎁Packages", callback_data="3")],
            [InlineKeyboardButton("⚠Disclaimer", callback_data="4")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(
            chat_id,
            text="Hello <b>{}</b> 😊\n\nI'm TMS's JARVIS 🤖\n\nWelcome to 𝑻𝒓𝒖𝒔𝒕𝒎𝒚𝒔𝒕𝒐𝒄𝒌'𝒔 𝑽𝑰𝑷 𝑪𝑯𝑨𝑻".format(
                username,
            ),
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
        )
    except Exception as e:
        print(e)
        if e.message == "Forbidden: bot was blocked by the user":
            keyboard = [
                [
                    InlineKeyboardButton(
                        "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                    ),
                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_text(
                text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                reply_markup=reply_markup,
            )
        else:
            update._effective_message.reply_text(
                text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
            )


def about_member(update: Update, context: CallbackContext):
    chat_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username

    try:
        bot.send_message(
            chat_id=chat_id,
            text="<i>TMS PROFILE</i>\n\n👤 Your Name: <b>{}</b>\n\n📅 Date Joined: <b>{}</b>\n\n✅ Your Instagram: <b>{}</b>\n\n💰 Your Package: <b>{}</b>\n\n".format(
                str([first_name if first_name else last_name][0])
                + " "
                + str([last_name if last_name else ""][0]),
                "Will be updated soon",
                "Will be updated soon",
                "Will be updated soon",
            ),
            parse_mode=ParseMode.HTML,
        )
    except TelegramError as e:
        if e.message == "Forbidden: bot was blocked by the user":
            keyboard = [
                [
                    InlineKeyboardButton(
                        "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                    ),
                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(
                text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                reply_markup=reply_markup,
            )
        else:
            update.message.reply_text(
                text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
            )


def help(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username
    try:
        keyboard = [
            [InlineKeyboardButton("👤About Me", callback_data="1")],
            [InlineKeyboardButton("📜Rules", callback_data="2")],
            [InlineKeyboardButton("🎁Packages", callback_data="3")],
            [InlineKeyboardButton("⚠Disclaimer", callback_data="4")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(
            chat_id=chat_id,
            text="Hello @{} 😊\n\nHow can I help you?".format(
                str([username if username else first_name or last_name][0]) + " "
            ),
            reply_markup=reply_markup,
        )
    except Exception as e:
        print(e)
        if e.message == "Forbidden: bot was blocked by the user":
            keyboard = [
                [
                    InlineKeyboardButton(
                        "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                    ),
                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_text(
                text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                reply_markup=reply_markup,
            )
        else:
            update._effective_message.reply_text(
                text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
            )


def welcome_new_member(update: Update, context: CallbackContext):

    for member in update.message.new_chat_members:
        chat_id = update.message.chat.id
        first_name = member.first_name
        last_name = member.last_name
        username = member.username

        try:
            keyboard = [
                [
                    InlineKeyboardButton(
                        "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                    ),
                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            bot.send_photo(
                chat_id=chat_id,
                photo="https://media.istockphoto.com/vectors/colorful-typography-banner-vector-id1172141868?k=6&m=1172141868&s=612x612&w=0&h=BxvixysXTEaDyu0Xin3ktuBWkV8a4SOm7isACzqyOCw=",
                caption="Welcome @{} 😊\n\nI'm TMS's JARVIS 🤖\n\nWelcome to 𝑻𝒓𝒖𝒔𝒕𝒎𝒚𝒔𝒕𝒐𝒄𝒌'𝒔 𝑽𝑰𝑷 𝑪𝑯𝑨𝑻 📈\n\nYou can access me by Cliking on the button below 😊".format(
                    str([username if username else first_name or last_name][0]) + " "
                ),
                reply_markup=reply_markup,
            )
            # bot.send_message(
            #     chat_id=chat_id,
            #     text="Welcome @{} 😊\n\nI'm TMS's JARVIS 🤖\n\nWelcome to 𝑻𝒓𝒖𝒔𝒕𝒎𝒚𝒔𝒕𝒐𝒄𝒌'𝒔 𝑽𝑰𝑷 𝑪𝑯𝑨𝑻 📈\n\nYou can access me by Cliking on the button below 😊".format(
            #         str([username if username else first_name or last_name][0]) + " "
            #     ),
            #     reply_markup=reply_markup,
            # )
        except Exception as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )


# bot.send_message(chat_id="-452615448", text="Welcome to")

updater.dispatcher.add_handler(
    MessageHandler(Filters.status_update.new_chat_members, welcome_new_member)
)
# start_value = CommandHandler("start", welcome)


def handle_message(update: Update, context: CallbackContext):
    chat_id = update._effective_message.chat.id
    first_name = update._effective_message.chat.first_name
    last_name = update._effective_message.chat.last_name
    username = update._effective_message.chat.username

    text = str(update.effective_message.text).lower()
    if text == "help" or "/help" in text:
        try:
            keyboard = [
                [InlineKeyboardButton("👤About Me", callback_data="1")],
                [InlineKeyboardButton("📜Rules", callback_data="2")],
                [InlineKeyboardButton("🎁Packages", callback_data="3")],
                [InlineKeyboardButton("⚠Disclaimer", callback_data="4")],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_text(
                text="Hello How can I help you?\n",
                reply_markup=reply_markup,
            )
        except Exception as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )

    if "hello" in text or "hi" in text or "hey" in text or "jarvis" in text or "j.a.r.v.i.s" in text:
        try:
            keyboard = [
                [InlineKeyboardButton("👤About Me", callback_data="1")],
                [InlineKeyboardButton("📜Rules", callback_data="2")],
                [InlineKeyboardButton("🎁Packages", callback_data="3")],
                [InlineKeyboardButton("⚠Disclaimer", callback_data="4")],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_animation(
                animation="https://media.giphy.com/media/PRVDslxfTmwXkLinrk/giphy.gif",
                caption="Hello 😊\n\nI'm TMS's JARVIS 🤖\n\nHow can I help you?",
                reply_markup=reply_markup,
            )

            # update._effective_message.reply_text(
            #     text="Hello 😊\n\nI'm TMS's JARVIS 🤖\n\nHow can I help you?",
            #     reply_markup=reply_markup,
            # )
        except Exception as e:
            print(e)
            if e.message == "Forbidden: bot was blocked by the user":
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "Start TMS-JARVIS 🚀", url="https://t.me/TMSVIP_BOT"
                        ),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                update._effective_message.reply_text(
                    text="Uh! You might have blocked or have not Started JARVIS\n\nSTART him by clicking the button below 😊",
                    reply_markup=reply_markup,
                )
            else:
                update._effective_message.reply_text(
                    text="Uh! There is a technical problem with JARVIS, We'll rectify it soon.\n\nSorry For your Inconvenience"
                )


dispatcher.add_handler(CommandHandler("me", about_member))
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("packages", packages))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()