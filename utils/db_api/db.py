from utils.misc.datetime_now import _get_now_datetime
import sqlite3


class DataBase:
    def __init__(self, path_to_db='finance_bot.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def cursor(self):
        return self.connection.cursor()

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def _init_db(self):
        """Инициализирует БД"""
        with open("utils/db_api/create_db.sql", "r") as f:
            sql = f.read()
        self.cursor().executescript(sql)
        self.connection.commit()

    def check_db(self):
        if self.execute("SELECT name FROM sqlite_master "
                        "WHERE type='table' AND name='expense'", fetchall=True):
            return
        self._init_db()

    def select_all_categories(self):
        sql = """
                SELECT * FROM category
                """
        return self.execute(sql, fetchall=True)

    def add_expense(self, amount: int, created, category_codename: str, raw_test: str):
        sql = """
        INSERT INTO expense(amount, created, category_codename, raw_text ) VALUES (?, ?, ?, ? )
        """
        parameters = (amount, created, category_codename, raw_test)
        self.execute(sql, parameters=parameters, commit=True)

    def delete(self, table: str, row_id: int) -> None:
        row_id = int(row_id)
        sql = f"DELETE FROM {table} WHERE id={row_id}"
        return self.execute(sql, commit=True)

    def last_expenses(self):
        sql = """
        SELECT id, amount, category_codename FROM expense ORDER BY created DESC LIMIT 10
        """
        return self.execute(sql, fetchall=True)

    def get_month_statistic(self):
        now = _get_now_datetime()
        first_day_of_month = f"{now.year}-{now.month:02}-01"
        sql = f"""
        SELECT sum(amount) FROM expense where date(created) >= {first_day_of_month}
        """
        result = self.execute(sql, fetchone=True)
        if not result[0]:
            return "В цьому місяці не має витрат"
        all_month_expenses = result[0]
        return (f'Витрати в цьому місяці - {all_month_expenses} грн')

    def get_today_statistic(self):
        sql = f"""
        SELECT SUM(amount) FROM expense WHERE date(created)=date('now', 'localtime')
        """
        result = self.execute(sql, fetchone=True)
        if not result[0]:
            return 'Сьогодні ще не має витрат'
        all_today_expenses = result[0]
        return f'Сьогодні ви витратили - {all_today_expenses} грн'
