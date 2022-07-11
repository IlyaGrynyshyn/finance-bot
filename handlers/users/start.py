from aiogram import types

from loader import dp

@dp.message_handler(commands=['start', 'help'])
async def bot_start(message: types.Message):
    """ Відправляємо вітальне повідомлення і допомога по боту"""
    text = "Бот для обліку фінансів \n" \
           "Додати витрати: 500 бензин \n" \
           "Сьогоднішня статистика: /today \n" \
           "Місячна статистика: /month \n" \
           "Останні внесені витрати: /expenses \n" \
           "Категорії витрат \n"
    await message.answer(text)
