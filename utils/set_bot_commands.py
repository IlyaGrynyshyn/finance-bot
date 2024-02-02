from aiogram import types


async def set_default_commands(dp):
    """
    Вивід всіх команд
    :param dp:
    :return:
    """
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вивести справку"),
            types.BotCommand("expenses", "Останні витрати"),
            types.BotCommand("today", "Останні витрати за поточний день"),
            types.BotCommand("month", "Виводить всі трати за поточний місяць"),
        ]
    )
