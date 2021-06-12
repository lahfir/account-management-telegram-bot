import time
from datetime import datetime
import pymongo
import telegram
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from telegram import *
from telegram import TelegramError
from telegram.ext import *
from telegram_bot_calendar import LSTEP, DetailedTelegramCalendar

cluster = MongoClient(
    "mongodb+srv://lahfir:mslahfir%40262001@clustertms.lkxcy.mongodb.net/test?authSource=admin&replicaSet=atlas-xqmx6k-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
)
if cluster:
    print("Connected")

db = cluster["tms"]
collection = db["members"]

model = {
    "_id": "",
    "name": "",
    "doj": "",
    "registered": "",
    "approved": "",
    "teleusername": "",
    "instausername": "",
    "package": "",
}

# my_id = 1243113998
# tms = 879137704

bot = Bot("1849417198:AAHR2-o8d20OJ4sVzBMuHbcj8_ZEzHCpMZs")
updater = Updater("1849417198:AAHR2-o8d20OJ4sVzBMuHbcj8_ZEzHCpMZs", use_context=True)

dispatcher = updater.dispatcher

# chat.id sends in group whit from_user.id send [private]


def sendToIndividual(chat_id, text):
    bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)


def rules():
    rules = """🟢 TMS RULES\n\nMoving forward if we put either of these symbols 🚀✅ after saying SELL with a picture of the stock it means we are selling the stock! 


____________________________


Don’t forget to follow our Twitter  @trustmystocks as we provide constant updates. 
(every follow helps)

____________________________

You must be aware of Risk Management when Trading. You CANNOT get carried away on any one given Signal. That would be a ROOKIE mistake and can be very costly.  Stocks go in two directions and you must be prepared to sustain certain losses without bankrupting your bankroll. 

You should always allocate one unit for trades unless told otherwise. One unit should comprise 5%-8% of your total stock investment bankroll (i.e. if you have $1000 in your bankroll you should only be trading approximately $50-$80 per stock signal). We preach this often so you can invest in more signals. 

You must also be patient.  Other advisers may be very aggressive in taking your money and pumping out stock picks non-stop all day. However, once you’re BROKE they forget about you and move on to new customers.  We take the long term approach because we want you as part of our family for a long time. Our clients should be looking at their stock investments as a way of life not a get rich overnight scheme. Yes some signals could go up 100% plus, but you have to maintain  realistic expectations. We are not gambling; we are investing. 

The market does not only go up. It feels like that sometimes when we’re on a roll but that doesn’t continue forever.  That’s impossible. If it was that easy the whole world would be millionaires. The smart money gets rich slow and steady. Week after week and month after month.

-
-
Trading strategies!

Trailing Stop 

It is called a “trailing stop-loss order”.  This is a valuable strategy to utilize when our stock picks increase in value. 
 
You’re all familiar with a standard “stop-loss order” in which you pre-set an automatic sell number if a stock dips to that certain number.  But what if a stocks rises?  How do you lock in a guaranteed positive return while still allowing for potential continued upward profit? One method is the “80/20” rule that we used successfully numerous times already (see below for more details). 

Another method is the “trailing stop-loss order”.   Let’s say you buy a recommended stock at $10.00.  We may tell you the stop-loss is $9.00 (which is 10%).   But what if the stock goes up?  We may now also advise a 10% trailing stop-loss order.  That means your brokerage account will permit the stock to continue to rise but sell it in the future only if it ever dips more than 10% from that current price. 

So if that $10.00 stock reaches let’s say $13.00 it will automatically sell if the stock then goes below $11.70. In this scenario you are guaranteeing yourself a 17% increase ($10.00 to $11.70) while at the same time letting the stock continue to ride if it hits $15.00 and keeps going up or at least never dips to below $11.70. If the stock keeps rising to $20.00 for example it will only be sold if it goes below $18.00 (10% loss) and you will have locked in 80% profit ($10.00 to $18.00). 

Sometimes we may advise a 10% trailing stop-loss order, other times it could be 15% or 20% or some other percentage. It depends on the specific stock. Main benefit is it secures profits. 

It is a prudent investment strategy that the top (and most expensive) stock advisors utilize it at the major investment firms.  There is no reason why our family should not be using it too.  

Our job is not only find winning stocks but also to share time proven investment techniques.

-
-
80/20 Strategy 

The 80/20 strategy is as follows:
 
Let’s say we recommended you buy a stock at $100/share, and set the take profit at $110. The stock hits $110.00 (10% profit).  If you are happy with the 10% (and nothing is wrong with a nice 10% profit especially when the banks are paying only 1% interest for a whole year of your money) then take your profit and congratulations."""

    rules2 = """However,  we recommend that you consider the 80/20 stop/loss play.  In that case, you sell 80% of it now.  

Example of 80/20 Sell:

So you bought one share at $100
It went up 10% 
You now have $110
You sell 80% of that ($88)
So you now have $88 back in cash and $22 in your portfolio 
You made 10% on that first $80 ($88 that you’re actually taking now) and 10% on that other $20 ($22 but it’s still in the stock)

This system allows for the final 20% ($22) to either grow more if the stock skyrockets or if it falls a little bit you get ready to sell it. 
If the stock continues to skyrocket you can take it out whenever you see fit but if the stock drops by 5% we recommend that you sell it and lock in a guaranteed overall profit on the stock deal.  

So the 80/20 rule allows for some possibly big time gains but also guarantees a profit even though less profit than if you sold all 100% at $110.  
 
Everybody’s profit margin satisfaction and risk comfort level is different so there cannot be a one size fits all plan.  If you’re conservative take your profit and run.  If you’re more aggressive then play it out with the 20% and swing for the fences."""

    return [rules, rules2]


def calendar(update: Update, context: CallbackContext):
    bot.send_chat_action(chat_id=update.message.chat.id, action="typing")
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(
        update.message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar
    )


def calendar1(update: Update, context: CallbackContext):
    bot.send_chat_action(chat_id=update._effective_message.chat.id, action="typing")
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(
        update._effective_message.chat.id,
        f"Select {LSTEP[step]}",
        reply_markup=calendar,
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
        result = result.strftime("%m-%d-%y")
        bot.edit_message_text(
            f"🚨 <b>TMS SIGNAL</b> 🚨\n\nDate: {result}\n\nTicker: \n\nCurrent Price: \n\nDirection: \n\nOptional STOP @ \n\nTake Profit @",
            update._effective_message.chat.id,
            update._effective_message.message_id,
            parse_mode=ParseMode.HTML,
        )
    return ConversationHandler.END


def button(update: Update, context: CallbackContext):
    global memberName, memberUsername, memberInstagram, memberChatId, memberTeleUsername, memberPackage, memberDoj, memberRegistered, memberApproved

    query = update.callback_query
    chat_id = update._effective_user.id
    message_id = update._effective_message.message_id
    first_name = update._effective_user.first_name
    last_name = update._effective_user.last_name
    username = update._effective_user.username
    query.answer()

    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choice = query.data
    bot.send_chat_action(chat_id, action="typing")

    # Now u can define what choice ("callback_data") do what like this:
    if choice == "1":
        try:
            for x in collection.find({"_id": chat_id}):
                if x["registered"] == "Y":
                    bot.send_message(
                        chat_id=chat_id,
                        text="<i>TMS PROFILE</i>\n\n👤 Your Name: <b>{}</b>\n\n📅 Date Joined: <b>{}</b>\n\n✅ Your Instagram: <b>{}</b>\n\n💰 Your Package: <b>{}</b>\n\n\n✅ Approved: <b>{}</b>".format(
                            x["name"],
                            x["doj"],
                            x["instausername"],
                            x["package"],
                            ["Yes" if x["approved"] == "Y" else "No"][0],
                        ),
                        parse_mode=ParseMode.HTML,
                    )
                    memberRegistered = "Y"
                else:
                    memberRegistered = "N"
                    keyboard = [
                        [
                            InlineKeyboardButton(
                                "👤New User Registration", callback_data="new-reg"
                            )
                        ]
                    ]

                    reply_markup = InlineKeyboardMarkup(keyboard)
                    bot.send_message(
                        chat_id=chat_id,
                        text="Seems like you haven't registered, Register now by clicking the button below",
                        reply_markup=reply_markup,
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
                text=rules()[0],
                parse_mode=ParseMode.HTML,
            )
            bot.send_message(
                chat_id=chat_id,
                text=rules()[1],
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

These are the prices for the <b>VIP Chat</b>
<b>
•  Monthly Rates - <i>$149.99</i>
•  3 Month Rate  - <i>$299.99</i>
•  6 Month Rate. - <i>$499.99</i>
•  Yearly Rates    - <i>$999.99</i>
</b>
💳 Payment Method: <b>(PayPal, Zelle, Venmo)</b>

GET OFF THE SIDELINES AND RIDE OUR SIGNALS EVERY DAY 🚂🤝""",
                parse_mode=ParseMode.HTML,
                animation="https://media.giphy.com/media/fULcqyLb74wqHdd1gW/giphy.gif",
            )
        #             bot.send_message(
        #                 chat_id,
        #                 text="""🎁 TMS PACKAGES

        # These are the prices for the <b>VIP Chat</b>
        # <b>
        # •  Monthly Rates - <i>$149.99</i>
        # •  3 Month Rate  - <i>$299.99</i>
        # •  6 Month Rate. - <i>$499.99</i>
        # •  Yearly Rates    - <i>$999.99</i>
        # </b>
        # 💳 Payment Method: <b>(PayPal, Zelle, Venmo)</b>

        # GET OFF THE SIDELINES AND RIDE OUR SIGNALS EVERY DAY 🚂🤝""",
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
    elif choice == "5":
        bot.send_chat_action(chat_id, action="typing")
        if choice == "5":
            try:
                bot.send_chat_action(chat_id, action="typing")
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "👤New User Registration", callback_data="new-reg"
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "🚀Signal Search", callback_data="signal-search"
                        )
                    ],
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                bot.send_message(
                    text="<b>\n⚙ Options\n</b>",
                    chat_id=chat_id,
                    reply_markup=reply_markup,
                    parse_mode=ParseMode.HTML,
                )
            except Exception as e:
                print(e)
    elif choice == "new-reg":
        try:
            for x in collection.find({"_id": chat_id}):
                if x["registered"] == "Y":
                    bot.send_message(
                        chat_id=chat_id,
                        text="You have already registered. You can access your profile with /me command.\n\n If you want to edit your profile or extend the package, contact @trustmystocks.\n\nOption for extending the package through bot is <b>Coming Soon....</b> 💥",
                        parse_mode=ParseMode.HTML,
                    )
                else:
                    bot.send_message(chat_id=chat_id, text="Enter your name")
                    return NAME
        except Exception as e:
            print(e)
    elif choice == "signal-search":
        try:
            for x in collection.find({"_id": chat_id}):
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "👤New User Registration", callback_data="new-reg"
                        )
                    ]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                if x["registered"] == "Y":
                    if x["approved"] == "Y":
                        keyboard = [
                            [
                                InlineKeyboardButton("Today", callback_data="today"),
                                InlineKeyboardButton(
                                    "Calendar", callback_data="calendar"
                                ),
                            ]
                        ]
                        reply_markup = InlineKeyboardMarkup(keyboard)
                        bot.send_message(
                            chat_id=chat_id,
                            text="Please select a date to see the signals. Select Today to see today's signal or select Calendar to see the signal on that particular date",
                            parse_mode=ParseMode.HTML,
                            reply_markup=reply_markup,
                        )
                elif x["registered"] == "N":
                    bot.send_message(
                        chat_id=chat_id,
                        text="You haven't registered yet, Click on the button below to register 👇",
                        reply_markup=reply_markup,
                    )
                else:
                    bot.send_message(
                        chat_id=chat_id,
                        text="You aren't approved yet, We'll approve you ASAP. Thanks for your patience ☺",
                    )
        except Exception as e:
            print(e)
    elif choice == "today":
        bot.send_message(
            chat_id=chat_id,
            text=f"🚨 <b>TMS SIGNAL</b> 🚨\n\nDate: {datetime.now().strftime('%m-%d-%Y')}\n\nTicker: \n\nCurrent Price: \n\nDirection: \n\nOptional STOP @ \n\nTake Profit @",
            parse_mode=ParseMode.HTML,
        )
    elif choice == "calendar":
        calendar1(update, context)
    try:
        result, key, step = DetailedTelegramCalendar().process(
            update.callback_query.data
        )
        if not result and key:
            bot.edit_message_text(
                f"Select {LSTEP[step]}",
                update._effective_message.chat.id,
                update._effective_message.message_id,
                reply_markup=key,
            )
        elif result:
            result = result.strftime("%m-%d-%y")
            bot.edit_message_text(
                f"🚨 <b>TMS SIGNAL</b> 🚨\n\nDate: {result}\n\nTicker: \n\nCurrent Price: \n\nDirection: \n\nOptional STOP @ \n\nTake Profit @",
                update._effective_message.chat.id,
                update._effective_message.message_id,
                parse_mode=ParseMode.HTML,
            )
    except Exception as e:
        print()


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
            caption="""🎁 List of packages available with TMS

These are the prices for the <b>VIP Chat</b>
<b>
•  Monthly Rates - <i>$149.99</i>
•  3 Month Rate  - <i>$299.99</i>
•  6 Month Rate. - <i>$499.99</i>
•  Yearly Rates    - <i>$999.99</i>
</b>
💳 Payment Method: <b>(PayPal, Zelle, Venmo)</b>

GET OFF THE SIDELINES AND RIDE OUR SIGNALS EVERY DAY 🚂🤝""",
            parse_mode=ParseMode.HTML,
            animation="https://media.giphy.com/media/fULcqyLb74wqHdd1gW/giphy.gif",
        )
        #             bot.send_message(
        #                 chat_id,
        #                 text="""🎁 TMS PACKAGES

        # These are the prices for the <b>VIP Chat</b>
        # <b>
        # •  Monthly Rates - <i>$149.99</i>
        # •  3 Month Rate  - <i>$299.99</i>
        # •  6 Month Rate. - <i>$499.99</i>
        # •  Yearly Rates    - <i>$999.99</i>
        # </b>
        # 💳 Payment Method: <b>(PayPal, Zelle, Venmo)</b>

        # GET OFF THE SIDELINES AND RIDE OUR SIGNALS EVERY DAY 🚂🤝""",
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

    global memberChatId, memberUsername
    memberChatId = chat_id
    memberUsername = username

    print(memberChatId, memberUsername)

    model["_id"] = memberChatId
    model["teleusername"] = memberUsername
    model["approved"] = "N"
    model["registered"] = "N"

    try:
        results = collection.insert_one(model)
    except DuplicateKeyError as dke:
        print("Already registered")

    try:
        keyboard = [
            [InlineKeyboardButton("👤About Me", callback_data="1")],
            [InlineKeyboardButton("📜Rules", callback_data="2")],
            [InlineKeyboardButton("🎁Packages", callback_data="3")],
            [InlineKeyboardButton("⚠Disclaimer", callback_data="4")],
            [InlineKeyboardButton("⚙Options", callback_data="5")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(
            chat_id,
            text="Hello <b>{}</b> 😊\n\nI'm TMS's JARVIS 🤖\n\nWelcome to 𝑻𝒓𝒖𝒔𝒕𝒎𝒚𝒔𝒕𝒐𝒄𝒌'𝒔 𝑽𝑰𝑷 𝑪𝑯𝑨𝑻".format(
                str(["@" + username if username else first_name or last_name][0])
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

    global memberChatId
    memberChatId = chat_id

    try:
        for x in collection.find({"_id": chat_id}):
            if x["registered"] == "Y":
                bot.send_message(
                    chat_id=chat_id,
                    text="<i>TMS PROFILE</i>\n\n👤 Your Name: <b>{}</b>\n\n📅 Date Joined: <b>{}</b>\n\n✅ Your Instagram: <b>{}</b>\n\n💰 Your Package: <b>{}</b>\n\n\n✅ Approved: <b>{}</b>".format(
                        x["name"],
                        x["doj"],
                        x["instausername"],
                        x["package"],
                        ["Yes" if x["approved"] == "Y" else "No"][0],
                    ),
                    parse_mode=ParseMode.HTML,
                )
                memberRegistered = "Y"
            else:
                memberRegistered = "N"
                keyboard = [
                    [
                        InlineKeyboardButton(
                            "👤New User Registration", callback_data="new-reg"
                        )
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)
                bot.send_message(
                    chat_id=chat_id,
                    text="Seems like you haven't registered, Register now by clicking the button below",
                    reply_markup=reply_markup,
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

    global memberChatId
    memberChatId = chat_id
    try:
        keyboard = [
            [InlineKeyboardButton("👤About Me", callback_data="1")],
            [InlineKeyboardButton("📜Rules", callback_data="2")],
            [InlineKeyboardButton("🎁Packages", callback_data="3")],
            [InlineKeyboardButton("⚠Disclaimer", callback_data="4")],
            [InlineKeyboardButton("⚙Options", callback_data="5")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(
            chat_id=chat_id,
            text="Hello {} 😊\n\nHow can We help you?".format(
                str(["@" + username if username else first_name or last_name][0]) + " "
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

dispatcher.add_handler(
    MessageHandler(Filters.status_update.new_chat_members, welcome_new_member)
)
# start_value = CommandHandler("start", welcome)


def handle_message(update: Update, context: CallbackContext):
    chat_id = update._effective_message.chat.id
    first_name = update._effective_message.chat.first_name
    last_name = update._effective_message.chat.last_name
    username = update._effective_message.chat.username

    text = str(update.effective_message.text).lower()
    if text == "help" or "/help" in text or "/me" in text or "/packages" in text:
        try:
            keyboard = [
                [InlineKeyboardButton("👤About Me", callback_data="1")],
                [InlineKeyboardButton("📜Rules", callback_data="2")],
                [InlineKeyboardButton("🎁Packages", callback_data="3")],
                [InlineKeyboardButton("⚠Disclaimer", callback_data="4")],
                [InlineKeyboardButton("⚙Options", callback_data="5")],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_text(
                text="Hello How can We help you?\n",
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

    if (
        "hello" in text
        or "hi" in text
        or "hey" in text
        or "jarvis" in text
        or "j.a.r.v.i.s" in text
    ):
        try:
            keyboard = [
                [InlineKeyboardButton("👤About Me", callback_data="1")],
                [InlineKeyboardButton("📜Rules", callback_data="2")],
                [InlineKeyboardButton("🎁Packages", callback_data="3")],
                [InlineKeyboardButton("⚠Disclaimer", callback_data="4")],
                [InlineKeyboardButton("⚙Options", callback_data="5")],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            update._effective_message.reply_animation(
                animation="https://media.giphy.com/media/PRVDslxfTmwXkLinrk/giphy.gif",
                caption="Hello 😊\n\nI'm TMS's JARVIS 🤖\n\nHow can We help you?",
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


NAME, INSTAGRAM, PACKAGE, DOJ, TELEGRAM = range(5)

(
    memberName,
    memberUsername,
    memberInstagram,
    memberMobile,
    memberChatId,
    memberTeleUsername,
    memberPackage,
    memberDoj,
    memberRegistered,
    memberApproved,
) = ("", "", "", "", "", "", "", "", "", "")


def namehandler(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user

    keyboard = [
        [
            InlineKeyboardButton("✅Yes", callback_data="name-y"),
            InlineKeyboardButton("❌No", callback_data="name-n"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"Your Name: <b>{update.message.text}</b>",
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
    )


def instagramhandler(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user
    global memberInstagram

    memberInstagram = f"https://instagram.com/{update.message.text[1:]}"
    keyboard = [
        [
            InlineKeyboardButton("✅Yes", callback_data="insta-y"),
            InlineKeyboardButton("❌No", callback_data="insta-n"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"Your Instagram: {update.message.text}\n\nhttps://instagram.com/{update.message.text[1:]}",
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
    )


def telegramhandler(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user

    keyboard = [
        [
            InlineKeyboardButton("✅Yes", callback_data="telegram-y"),
            InlineKeyboardButton("❌No", callback_data="telegram-n"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"Your Telegram Username: @<b>{update.message.from_user.username}</b>",
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
    )


def dojhandler(update: Update, _: CallbackContext) -> int:
    user = update.message.from_user

    keyboard = [
        [
            InlineKeyboardButton("✅Yes", callback_data="doj-y"),
            InlineKeyboardButton("❌No", callback_data="doj-n"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"Your DOJ: {datetime.now().strftime('%m-%d-%Y')}",
        reply_markup=reply_markup,
    )


def calendardojhandler(update: Update, context: CallbackContext, result) -> int:
    global memberDoj
    memberDoj = result
    keyboard = [
        [
            InlineKeyboardButton("✅Yes", callback_data="doj-y"),
            InlineKeyboardButton("❌No", callback_data="doj-n"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update._effective_message.reply_text(
        f"Your DOJ: {result}",
        reply_markup=reply_markup,
    )


def databaseentry():
    collection.update_one(
        {"_id": memberChatId},
        {
            "$set": {
                "registered": "Y",
                "name": memberName,
                "doj": memberDoj,
                "instausername": memberInstagram,
                "package": memberPackage,
            }
        },
    )
    print(
        memberChatId,
        memberName,
        memberApproved,
        memberDoj,
        memberInstagram,
        memberPackage,
        memberUsername,
        memberRegistered,
        memberTeleUsername,
    )
    bot.send_message(
        chat_id=memberChatId,
        text="You can access our team by using the following commands.\n\n1. /help - We'll show all the available options\n2. /me - We'll show your TMS Profile\n3. /packages - We'll show the list of packages available in TMS",
    )


def packageselector(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    chat_id = update._effective_message.chat.id
    query.answer()
    choice = query.data

    global memberPackage

    if choice == "one_m":
        memberPackage = "$149.99/Month"
        keyboard = [
            [
                InlineKeyboardButton("✅Yes", callback_data="one-m-y"),
                InlineKeyboardButton("❌No", callback_data="one-m-n"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update._effective_message.reply_text(
            f"Your Package: <b>$149.99/Month</b>",
            reply_markup=reply_markup,
            parse_mode=ParseMode.HTML,
        )

    elif choice == "three_m":
        memberPackage = "$299.99/3 Months"
        keyboard = [
            [
                InlineKeyboardButton("✅Yes", callback_data="three-m-y"),
                InlineKeyboardButton("❌No", callback_data="three-m-n"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update._effective_message.reply_text(
            f"Your Package: <b>$299.99/3 Months</b>",
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
        )
    elif choice == "six_m":
        memberPackage = "$499.99/6 Months"
        keyboard = [
            [
                InlineKeyboardButton("✅Yes", callback_data="six-m-y"),
                InlineKeyboardButton("❌No", callback_data="six-m-n"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update._effective_message.reply_text(
            f"Your Package: <b>$499.99/6 Months</b>",
            reply_markup=reply_markup,
            parse_mode=ParseMode.HTML,
        )
    elif choice == "one_y":
        memberPackage = "$999.9/Year"
        keyboard = [
            [
                InlineKeyboardButton("✅Yes", callback_data="one-y-y"),
                InlineKeyboardButton("❌No", callback_data="one-y-n"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update._effective_message.reply_text(
            f"Your Package: <b>$999.99/Year</b>",
            reply_markup=reply_markup,
            parse_mode=ParseMode.HTML,
        )

    elif (
        choice == "one-m-y"
        or choice == "three-m-y"
        or choice == "six-m-y"
        or choice == "one-y-y"
    ):
        bot.send_message(
            chat_id,
            text="Registration is successful. You will receive a message from our team shortly. 😉\n\n <b>Welcome to TRUSTMYSTOCKS</b>",
            parse_mode=ParseMode.HTML,
        )
        databaseentry()
        return ConversationHandler.END
    elif (
        choice == "one-m-n"
        or choice == "three-m-n"
        or choice == "six-m-n"
        or choice == "one-y-n"
    ):
        bot.send_message(chat_id, text="Alright, Please select the Package correctly")
        return PACKAGE


def yes_no(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = update._effective_message.chat.id
    query.answer()
    choice = query.data

    global memberName, memberUsername, memberInstagram, memberMobile, memberChatId, memberTeleUsername, memberPackage, memberDoj

    if choice == "name-y":
        memberName = update._effective_message.text[11:]
        print(memberName)
        bot.send_message(chat_id, text="Now enter your instagram handle with @")
        return INSTAGRAM
    elif choice == "name-n":
        update._effective_message.reply_text("Alright, Enter your correct Name please")
        return NAME
    elif choice == "insta-y":
        print(memberInstagram)
        keyboard = [
            [KeyboardButton("@{}".format(update._effective_message.chat.username))]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        bot.send_message(
            chat_id,
            text="Now verify your Telegram Username by selecting on your keyboard",
            reply_markup=reply_markup,
        )
        return TELEGRAM
    elif choice == "insta-n":
        bot.send_message(
            chat_id, text="Alright, Enter your correct Instagram Handle please"
        )
        return INSTAGRAM
    elif choice == "telegram-y":
        keyboard = [[KeyboardButton("/today"), KeyboardButton("/calendar")]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        bot.send_message(
            chat_id,
            text="Now Select Date of Joining. Select /today if you've joined today or to select a date click on /calendar",
            reply_markup=reply_markup,
            parse_mode=ParseMode.HTML,
        )
        ReplyKeyboardRemove()
        return DOJ
    elif choice == "telegram-n":
        bot.send_message(chat_id, text="Alright, Enter your Telegram Username please")
        return TELEGRAM
    elif choice == "doj-y":
        memberDoj = update._effective_message.text[10:]
        print(memberDoj)
        keyboard = [
            [InlineKeyboardButton("$149.99/Month", callback_data="one_m")],
            [InlineKeyboardButton("$299.99/3 Months", callback_data="three_m")],
            [InlineKeyboardButton("$499.99/6 Months", callback_data="six_m")],
            [InlineKeyboardButton("$999.99/ Year", callback_data="one_y")],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(
            chat_id,
            text="Alright we are almost at the end of the registration process 😊\n\nNow Select the Package You've Selected",
            reply_markup=reply_markup,
            parse_mode=ParseMode.HTML,
        )
        return PACKAGE
    elif choice == "doj-n":
        bot.send_message(chat_id, text="Alright, Please select the date correctly")
        return DOJ

    result, key, step = DetailedTelegramCalendar().process(update.callback_query.data)
    if not result and key:
        bot.edit_message_text(
            f"Select {LSTEP[step]}",
            update._effective_message.chat.id,
            update._effective_message.message_id,
            reply_markup=key,
        )
    elif result:
        result = result.strftime("%m-%d-%y")
        bot.edit_message_text(
            f"You selected {result}",
            update._effective_message.chat.id,
            update._effective_message.message_id,
        )
        calendardojhandler(update, context, result)


def cancel(update: Update, _: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    update.message.reply_text(
        "Cancelled the Operation", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def todaysignal(update: Update, _: CallbackContext) -> int:
    update.message.reply_text(
        f"🚨 <b>TMS SIGNAL</b> 🚨\n\nDate: {datetime.now().strftime('%m-%d-%Y')}\n\nTicker: \n\nCurrent Price: \n\nDirection: \n\nOptional STOP @ \n\nTake Profit @",
        parse_mode=ParseMode.HTML,
    )
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(button)],
    states={
        NAME: [MessageHandler(Filters.text, namehandler), CallbackQueryHandler(yes_no)],
        INSTAGRAM: [
            MessageHandler(Filters.text, instagramhandler),
            CallbackQueryHandler(yes_no),
        ],
        TELEGRAM: [
            MessageHandler(Filters.text, telegramhandler),
            CallbackQueryHandler(yes_no),
        ],
        DOJ: [
            CommandHandler("today", dojhandler),
            CallbackQueryHandler(yes_no),
            CommandHandler("calendar", calendar),
        ],
        PACKAGE: [CallbackQueryHandler(packageselector)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

dispatcher.add_handler(CommandHandler("me", about_member))
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("packages", packages))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(CallbackQueryHandler(button))
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

while True:
    try:
        updater.start_polling()
        updater.idle()
    except ConnectionError as c:
        time.sleep(5)
