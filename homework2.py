from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
import telebot
import logging
import asyncio

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = telebot.TeleBot('')

# Хэндлер на команду /start
@bot.message_handler(commands=['start'])
def handle_start(message):
  bot.reply_to(message, 'Привет! Я бот помогающий твоему здоровью.')


@bot.message_handler(content_types=['text', 'photo', 'sticker'])
def handle_message(message):
        # Ответ на текстовое сообщение
        if message.text == 'Привет':
                bot.send_message(message.chat.id, 'Привет! Как дела?')
        if message.text == "Плохо":
                bot.send_message(message.chat.id, 'Ничего, наладится')


@bot.message_handler()
async def all_messages(message):
    # print(type(message))
    # print(f'Получено сообщение: {message}')
    print('Введите команду /start, чтобы начать общение.')

bot.polling()


