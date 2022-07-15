from aiogram import types
from loader import dp, db


@dp.message_handler(commands=['expenses'])
async def list_expenses(message: types.Message):
    """ Виводить список з 10 останніх витрат"""
    last_expenses = db.last_expenses(message.from_user.id)
    if not last_expenses:
        await message.answer('Росходів ще не має')
        return
    last_expenses_rows = [
        f"{expense[2]} грн в категорії  {expense[3]} — натисни "
        f"/del{expense[0]} для видалення"
        for expense in last_expenses]
    answer_message = "Останні витрати:\n\n * " + "\n* " \
        .join(last_expenses_rows)
    await message.answer(answer_message)
