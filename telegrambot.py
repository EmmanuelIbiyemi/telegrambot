# 8105723312:AAH4qdo4jRVC9m7gSU185ONMcuwp7cIsodc
# The Combind text figure above it a telegram bot api


from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ContextTypes
)

API_Key : str = "8105723312:AAH4qdo4jRVC9m7gSU185ONMcuwp7cIsodc"



# This is for the bottom menu
reply_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("MENTORSHIP")],
        [KeyboardButton("VIP SIGNALS")],
        [KeyboardButton("PHYSICAL CLASS")]
    ],
    resize_keyboard=True
)
#  ---- THIS IS FOR THE FUNCTIONS IN THE BOT


# --- These are all the command for the bot
# start
# help
# join
# settings
# subscribe
# membershipstatus

# --- THIS ARE THE MAIN FUNCTIONS COMMAND FOR THE BOT TO RESPOND TO
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) :

    await update.message.reply_text(f'Hello and Welcome {update.effective_user.first_name}', reply_markup=reply_keyboard)
    await update.message.reply_text("I am the Forex Bulls assistant bot \n"+
                                    "Which services are you interested in?")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    
    await update.message.reply_text("Below you'll find a list with the commands available in this bot \n"+
                    "OTHERS \n"+
                    "/MENTORSHIP \n" +
                    "/VIP_SIGNALS \n"+
                    "/PHYSICAL_CLASS \n"+
                    "GENERAL \n" +
                    "/help \n"
                    "Open the help menu. \n" +
                   " /settings - Change the way you interact with this bot.\n" +
                    "/start - Get started - show the initial message.\n" +
                   " SUBSCRIPTION \n" +
                    "/join - Join the channels or groups.\n" +
                   " /membershipstatus - Renew or cancel your subscription.\n" +
                    "/subscribe - Become a member.")

async def join_command(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    reply_button = [
        [InlineKeyboardButton("Subscribe", callback_data="subscribe")],
        [InlineKeyboardButton("🔁 Back To Main Menu", callback_data="main_menu")]
    ]

    reply_markup = InlineKeyboardMarkup(reply_button)
    await update.message.reply_text("You will need to subscribe to become a member.", reply_markup=reply_markup)

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    reply_buttoni = [
        [InlineKeyboardButton("UI Settings", callback_data="language_settings")],
        [InlineKeyboardButton("🔁 Back To Main Menu", callback_data="main_menu")]
    ]

    reply_markup = InlineKeyboardMarkup(reply_buttoni)
    await update.message.reply_text("Please select an option from the list below", reply_markup=reply_markup)

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) :

    button = [
        [InlineKeyboardButton("🔁 Back To Main Menu", callback_data="main_menu")]
    ]

    reply_markup = InlineKeyboardMarkup(button)

    await update.message.reply_text(
                                "Ready to get Access to the exclusive VIP group🔥🔥🔥\n"+
                                "\n"+
                               " You will have access to: \n"+
                                "💰 85% winrate on all trades.\n"+
                                "💰1:3 Risk to Reward.\n"+
                                "💰2-3 daily setups on XAUUSD, GBPUSD, GBPJPY and other pairs.\n"+
                                "\n"+
                                "https://forexbullsacademy.com/forexbulls-signals\n"+
                                "\n"+
                                "See you in the INNER CIRCLE ⭕️🚀"
                                , reply_markup=reply_markup)

async def membershipstatus(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    reply_button = [
        [InlineKeyboardButton("Subscribe", callback_data="subscribe")],
        [InlineKeyboardButton("🔁 Back To Main Menu", callback_data="main_menu")]
    ]

    reply_markup = InlineKeyboardMarkup(reply_button)
    await update.message.reply_text("You will need to subscribe to become a member.", reply_markup=reply_markup)


# This function to collect query for the user when a button is being clicked
# And also for the keyboard button on the phone keyboard
async def keyboard_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper()

    if text == "MENTORSHIP":
        reply_text = (
            "THE FOREX PROFIT ACCELERATOR 🚀:\n"+
            "Join TODAY For ONLY $197 And Get Access To:\n"+
            "✅ Proven Trading Systems – Start profiting with simple, step-by-step strategies.\n"+
            "✅ Direct Mentorship From 4 Millionaire Forex Traders – Get insider secrets that deliver fast results.\n"+
            "✅ 12 Weeks Private Community Access\n"+
            "✅ VIP Trade Signals – Profit immediately while mastering the system.\n"+
            "✅ 24/7 Expert Support – Never trade alone—help is always available.\n"+
            "✅ Live Trading Webinars – Watch trades unfold live and replicate them instantly.\n"+
            "✅ Weekly Q&A Sessions – Get answers fast and eliminate trading confusion.\n"+
            "✅ Lifetime Access To Course Material & Updates – Keep tools and strategies forever to grow at your pace.\n"+
            "This is a one-time purchase—LIFETIME ACCESS means you’ll enjoy ALL the benefits forever!\n"+
            "LIMITED SPOTS AVAILABLE – ACT NOW!\n"+
            "NOW $197 (WAS $497)\n"+
            "https://forexbullsacademy.com\n"
        )

    elif text == "VIP SIGNALS":
        reply_text = ("Ready to get Access to the exclusive VIP group🔥🔥🔥\n"+
                        "\n"+
                        "You will have access to: \n"+
                        "💰 85% winrate on all trades.\n"+
                        "💰1:3 Risk to Reward.\n"+
                        "💰2-3 daily setups on XAUUSD, GBPUSD, GBPJPY and other pairs.\n"+
                        "\n"+
                        "https://forexbullsacademy.com/forexbulls-signals\n"+
                        "\n"+
                        "See you in the INNER CIRCLE ⭕️🚀"
                      )

    elif text == "PHYSICAL CLASS":
        reply_text = ("To apply for Forex Bulls Exclusive physical classes \n"+
                        "\n"+
                      "Message @vidollarug or Call Us At 020 0907439 to book your slot"
                     )
    else:
        reply_text = "Sorry, I didn't understand that. Please choose a service from the keyboard."

    # Inline "Back to the main menu" button
    back_button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔁 Back to the main menu", callback_data='main_menu')]]
    )
    await update.message.reply_text(reply_text, reply_markup=back_button)


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # --------------------------------------------THIS IS FOR THE MAIN_MENU BUTTON---------------------------------------
    if query.data == "main_menu":
        await query.edit_message_text(
            text=(f"Hello and Welcome {update.effective_user.first_name} \n"+
                "\n"+
                "I am the Forex Bulls assistant bot \n" +
                "Which services are you interested in?"
                ),
    )

    # --------------------------------------------THIS IS FOR THE LANGUAGE BUTTON---------------------------------------
    elif query.data == "language_settings":
        language_button=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Select Language", callback_data="cl_language")],
                [InlineKeyboardButton("🔁 Back To Main Menu", callback_data="main_menu")]
            ]
        )

        reply_markup = language_button

        await query.edit_message_text(
            text=(f"Viewing UI Settings\n"+
                  "Please select the language you'd like to use from the list below\n"
                  ),
            reply_markup= reply_markup

        )


    # --------------------------------------------THIS IS FOR THE SUBSCRIBE BUTTON ---------------------------------------
    elif query.data == "subscribe":

        sub_button = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "Subscribe",
                callback_data="subscribe"
            )]]
        )


        reply_markup = sub_button

        await query.edit_message_text(
            text=("Ready to get Access to the exclusive VIP group🔥🔥🔥\n"+
                        "\n"+
                        "You will have access to: \n"+
                        "💰 85% winrate on all trades.\n"+
                        "💰1:3 Risk to Reward.\n"+
                        "💰2-3 daily setups on XAUUSD, GBPUSD, GBPJPY and other pairs.\n"+
                        "\n"+
                        "https://forexbullsacademy.com/forexbulls-signals\n"+
                        "\n"+
                        "See you in the INNER CIRCLE ⭕️🚀"
                      ),
            reply_markup= reply_markup
        )

    elif query.data == "cl_language":
        select_lan = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("English", callback_data="en")],
                [InlineKeyboardButton("Spanish", callback_data="spanish")],
                [InlineKeyboardButton("German", callback_data="German")],
                [InlineKeyboardButton("Arab", callback_data="arabic")],
                [InlineKeyboardButton("French", callback_data="french")],
                [InlineKeyboardButton("German", callback_data="german")],
                [InlineKeyboardButton("Arabic", callback_data="arabic")],
                [InlineKeyboardButton("Portuguese", callback_data="portuguese")],
                [InlineKeyboardButton("Italian", callback_data="italian")],
                [InlineKeyboardButton("Russian", callback_data="russian")],
                [InlineKeyboardButton("Hindi", callback_data="hindi")],
                [InlineKeyboardButton("Korean", callback_data="korean")],
                [InlineKeyboardButton("Swahili", callback_data="swahili")],
                [InlineKeyboardButton("Turkish", callback_data="turkish")],
                [InlineKeyboardButton("Mandarin", callback_data="chinese")],
                [InlineKeyboardButton("Dutch", callback_data="dutch")],
                [InlineKeyboardButton("Yoruba", callback_data="yoruba")],
                [InlineKeyboardButton("Igbo", callback_data="igbo")],
            ]
        )
        reply_markup = select_lan

        await query.edit_message_text(
            text=("Kindly Select Your Language:"),
            reply_markup=reply_markup
        )
# ----- THIS IS TO FOR THE APP BUILDER TO RUN THE PYTHON BOT CODE
app = ApplicationBuilder().token(API_Key).build()

#---- THIS IS FOR ALL THE COMMAND IN THE BOT
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("join", join_command))
app.add_handler(CommandHandler("settings", settings))
app.add_handler(CommandHandler("subscribe", subscribe))
app.add_handler(CommandHandler("membershipstatus", membershipstatus))

#----THIS IS A FUNCTION THAT IS USED FOR GETTING MESSAGE THAT THE KEYBOARD BUTTON SEND
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, keyboard_message))

#---- THIS IS HANDLE THE CALL_BACK IN THE BOT FOR THE MAIN MENU AND STUFF
app.add_handler(CallbackQueryHandler(handle_callback))
if app:
    print("Bot is starting")
app.run_polling()