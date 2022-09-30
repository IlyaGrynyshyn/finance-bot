from aiogram import types

from loader import dp, db, bot


@dp.message_handler(commands=['exportt'])
async def extort_to_csv(message: types.Message):
    file = db.export_to_csv(message.from_user.id)
    f = open(file, 'rb')
    await bot.send_document(chat_id=message.chat.id, document=f)
