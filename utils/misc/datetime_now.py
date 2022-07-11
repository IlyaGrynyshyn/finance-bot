from datetime import datetime

import pytz


def _get_now_datetime():
    timezone = pytz.timezone('Europe/Kiev')
    now = datetime.now(timezone)
    return now

def _get_now_formatted() -> str:
    """Возвращает сегодняшнюю дату строкой"""
    return _get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")