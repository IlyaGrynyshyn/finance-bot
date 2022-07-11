from utils.db_api.db import DataBase

db = DataBase()

def test():
    print('База даних успіщно створена')
    cat=  db.select_all_categories()

    db.last_expenses()
    print(db.last_expenses())
   # print(db.get_month_statistic())
    print(db.get_today_statistic())


test()

