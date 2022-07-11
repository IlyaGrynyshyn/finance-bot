from aiogram import types
from loader import dp, db


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def del_expense(message: types.Message):
    """ Видаляє однин запис з бази даних по її індефікатору """
    row_id = int(message.text[4:])
    db.delete('expense', row_id)
    await message.answer(f'Запис №{row_id} удалена')
