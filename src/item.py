import csv
from .errors import MyCustomError


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    @property
    def name(self):
        """Геттер для свойства name."""
        return self.__name

    @name.setter
    def name(self, value):
        """Сеттер для свойства name."""
        if len(value) > 10:
            raise MyCustomError("Название должно быть не более 10 символов")
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> list:
        """
        Инициализирует экземпляры класса Item данными из CSV-файла.

        :param file_path: Путь к CSV-файлу.
        :return: Список экземпляров класса Item.
        """
        items = []
        with open(file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                name = row["name"]
                price = cls.string_to_number(row["price"])
                quantity = int(row["quantity"])
                item = cls(name, price, quantity)
                items.append(item)
        return items

    @staticmethod
    def string_to_number(s: str) -> int:
        """
        Преобразует строку с числом в число типа float.

        :param s: Строка с числом.
        :return: Число типа int.
        """
        return int(float(s))
