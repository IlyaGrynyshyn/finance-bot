import asyncio

from aiogram import types
from aiogram.bot import bot

from loader import dp, db

import aioschedule
import time


async def noon_print():
    await dp.send_message("akfsd")


async def scheduler():
    aioschedule.every(1).second().do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())
