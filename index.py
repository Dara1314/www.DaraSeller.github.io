from telebot import TeleBot, types

# Initialize the bot with your token
bot = TeleBot("8063512390:AAHEIdKWZXdW4pFVrFB1Vcowq_a8yiP8jv0")

# Dictionary to store user balances
balances = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    account_button = types.KeyboardButton("🫂 Account")
    mobile_button = types.KeyboardButton("Mobile")
    free_fire_button = types.KeyboardButton("FreeFire")
    markup.row(account_button, mobile_button, free_fire_button)
    bot.send_message(
        message.chat.id, 
        "Hello! Welcome to Top Up Bot, How can I help you?", 
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "Mobile")
def mlbb(message):
    bot.reply_to(
        message, 
        """Products List Mobile Legend:

11 - $0.25
22 - $0.46
56 - $0.99
86 - $1.20
172 - $2.35
257 - $3.35
344 - $4.39
429 - $5.43
514 - $6.40
600 - $7.48
706 - $8.99
792 - $10.10
878 - $11.10
963 - $12.10
1050 - $13.45
1135 - $14.67
Weekly pass - $1.50

Example format order:
123456789 12345 Weekly
userid serverid item"""
    )

@bot.message_handler(func=lambda message: message.text == "🫂 Account")
def acc(message):
    user_username = message.from_user.username or "Unknown"
    user_id = message.from_user.id
    balance = balances.get(user_id, 0.0)  # Default balance is 0.0 if not found

    bot.send_message(
        message.chat.id, 
        f"ឈ្មោះគណនី : {user_username}\n"
        f"User Name : @{user_username}\n"
        f"Account ID : <code>{user_id}</code>\n"
        f"ចំនួនទឹកប្រាក់គណនី : {balance:.2f} $", 
        parse_mode="HTML"
    )

@bot.message_handler(func=lambda message: message.text == "FreeFire")
def FF(message):
    bot.reply_to(message, "Soon!")

# Start polling
if name == 'main':
    bot.polling()nh