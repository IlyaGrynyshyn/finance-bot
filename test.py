from utils.db_api.db import DataBase

db = DataBase()


def test():
    print("База даних успіщно створена")
    ab = db.check_user(159673949)
    if ab:
        print(ab)
    # print(db.get_month_statistic())
    print(db.get_today_statistic())


test()
