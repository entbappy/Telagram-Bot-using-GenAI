from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging
import openai

load_dotenv()
TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Connect with OpenAI
openai.api_key = OPENAI_API_KEY

# print("Ok")

MODEL_NAME = "gpt-3.5-turbo"

#Initialize bot 
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


