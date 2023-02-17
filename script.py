import openai
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Set up your OpenAI API credentials
openai.api_key = "Enter Your Key"

# Set up a Telegram bot with your token
bot = telegram.Bot(token="telegram token key")

# Define a function to generate a response to user input
def generate_response(input_text):
    prompt = f"User: {input_text}\nAI:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# Define a function to handle messages from users
def handle_message(update, context):
    user_input = update.message.text
    bot_response = generate_response(user_input)
    update.message.reply_text(bot_response)

# Define a function to start the bot
def start_bot():
    updater = Updater("5669842983:AAFmHhLRpBkvbr2DiIL1fzcqYZf4_1vyx48")
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
    dispatcher.add_handler(message_handler)
    updater.start_polling()
    updater.idle()

# Start the bot
start_bot()
