from aiogram import types

from loader import dp, db, bot


@dp.message_handler(commands=['export'])
async def extort_to_csv(message: types.Message):
    file = db.export_to_csv(message.from_user.id)
    f = open(file, 'r')
    await bot.send_document(chat_id=message.from_user.id, document=f)
