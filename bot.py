import openai
import telebot
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user_input = message.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = "אירעה שגיאה. נסה שוב מאוחר יותר."
    bot.reply_to(message, answer)

bot.polling()
