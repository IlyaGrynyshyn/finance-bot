from typing import List, NamedTuple
from loader import db


class Category(NamedTuple):
    """
    Структура категорії
    """

    codename: str
    name: str
    aliases: List[str]


class Categories:
    def __init__(self):
        self._categories = db.select_all_categories()

    def get_all_categories(self) -> List[Category]:
        """Повертає всі категорії"""
        return self._categories

    def get_categories(self, category_name: str) -> Category:
        """Повертає категорію по дному з її aliases"""
        finded = None
        other_category = None
        for category in self._categories:
            if category[0] == "other":
                other_category = category
            for alias in category:
                if category_name in str(alias):
                    finded = category[1]
        if not finded:
            finded = other_category[1]
        return finded
