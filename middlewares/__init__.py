from aiogram import Dispatcher

from data import config
from loader import dp
from .throttling import ThrottlingMiddleware
from .user_access import AccessMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    # dp.middleware.setup(AccessMiddleware(config.USER_ACCESS))
