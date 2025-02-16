class Guitar:
    """
    Базовый класс для гитар.

    Атрибуты:
        brand (str): Бренд гитары.
        model (str): Модель гитары.
        price (float): Цена гитары.
        _serial_number (str): Серийный номер гитары (инкапсулирован).

    Методы:
        __init__(brand: str, model: str, price: float, serial_number: str) -> None:
            Конструктор для инициализации гитары.
        __str__() -> str:
            Возвращает строковое представление гитары.
        __repr__() -> str:
            Возвращает официальное строковое представление гитары.
        play() -> str:
            Возвращает строку, имитирующую игру на гитаре.
        get_serial_number() -> str:
            Возвращает серийный номер гитары.
    """

    def __init__(self, brand: str, model: str, price: float, serial_number: str) -> None:
        """
        Конструктор для инициализации гитары.

        Аргументы:
            brand (str): Бренд гитары.
            model (str): Модель гитары.
            price (float): Цена гитары.
            serial_number (str): Серийный номер гитары.
        """
        self.brand = brand
        self.model = model
        self.price = price
        self._serial_number = serial_number  # Инкапсулированный атрибут

    def __str__(self) -> str:
        """
        Возвращает строковое представление гитары.

        Возвращает:
            str: Строковое представление гитары.
        """
        return f"Guitar(Brand: {self.brand}, Model: {self.model}, Price: ${self.price:.2f})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление гитары.

        Возвращает:
            str: Официальное строковое представление гитары.
        """
        return f"Guitar(brand='{self.brand}', model='{self.model}', price={self.price:.2f}, serial_number='{self._serial_number}')"

    def play(self) -> str:
        """
        Возвращает строку, имитирующую игру на гитаре.

        Возвращает:
            str: Строка, имитирующая игру на гитаре.
        """
        return "Playing the guitar..."

    def get_serial_number(self) -> str:
        """
        Возвращает серийный номер гитары.

        Возвращает:
            str: Серийный номер гитары.
        """
        return self._serial_number

class AcousticGuitar(Guitar):
    """
    Класс для акустических гитар, наследуется от Guitar.

    Атрибуты:
        wood_type (str): Тип дерева, из которого сделана гитара.

    Методы:
        __init__(brand: str, model: str, price: float, serial_number: str, wood_type: str) -> None:
            Конструктор для инициализации акустической гитары.
        __str__() -> str:
            Возвращает строковое представление акустической гитары.
        __repr__() -> str:
            Возвращает официальное строковое представление акустической гитары.
        play() -> str:
            Возвращает строку, имитирующую игру на акустической гитаре.
    """

    def __init__(self, brand: str, model: str, price: float, serial_number: str, wood_type: str) -> None:
        """
        Конструктор для инициализации акустической гитары.

        Аргументы:
            brand (str): Бренд гитары.
            model (str): Модель гитары.
            price (float): Цена гитары.
            serial_number (str): Серийный номер гитары.
            wood_type (str): Тип дерева, из которого сделана гитара.
        """
        super().__init__(brand, model, price, serial_number)
        self.wood_type = wood_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление акустической гитары.

        Возвращает:
            str: Строковое представление акустической гитары.
        """
        return f"AcousticGuitar(Brand: {self.brand}, Model: {self.model}, Price: ${self.price:.2f}, Wood Type: {self.wood_type})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление акустической гитары.

        Возвращает:
            str: Официальное строковое представление акустической гитары.
        """
        return f"AcousticGuitar(brand='{self.brand}', model='{self.model}', price={self.price:.2f}, serial_number='{self._serial_number}', wood_type='{self.wood_type}')"

    def play(self) -> str:
        """
        Возвращает строку, имитирующую игру на акустической гитаре.

        Возвращает:
            str: Строка, имитирующая игру на акустической гитаре.
        """
        return "Playing the acoustic guitar with a warm, natural sound..."

class ElectricGuitar(Guitar):
    """
    Класс для электрогитар, наследуется от Guitar.

    Атрибуты:
        pickup_type (str): Тип звукоснимателя.

    Методы:
        __init__(brand: str, model: str, price: float, serial_number: str, pickup_type: str) -> None:
            Конструктор для инициализации электрогитары.
        __str__() -> str:
            Возвращает строковое представление электрогитары.
        __repr__() -> str:
            Возвращает официальное строковое представление электрогитары.
        play() -> str:
            Возвращает строку, имитирующую игру на электрогитаре.
        amplify() -> str:
            Возвращает строку, имитирующую усиление звука электрогитары.
    """

    def __init__(self, brand: str, model: str, price: float, serial_number: str, pickup_type: str) -> None:
        """
        Конструктор для инициализации электрогитары.

        Аргументы:
            brand (str): Бренд гитары.
            model (str): Модель гитары.
            price (float): Цена гитары.
            serial_number (str): Серийный номер гитары.
            pickup_type (str): Тип звукоснимателя.
        """
        super().__init__(brand, model, price, serial_number)
        self.pickup_type = pickup_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление электрогитары.

        Возвращает:
            str: Строковое представление электрогитары.
        """
        return f"ElectricGuitar(Brand: {self.brand}, Model: {self.model}, Price: ${self.price:.2f}, Pickup Type: {self.pickup_type})"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление электрогитары.

        Возвращает:
            str: Официальное строковое представление электрогитары.
        """
        return f"ElectricGuitar(brand='{self.brand}', model='{self.model}', price={self.price:.2f}, serial_number='{self._serial_number}', pickup_type='{self.pickup_type}')"

    def play(self) -> str:
        """
        Возвращает строку, имитирующую игру на электрогитаре.

        Возвращает:
            str: Строка, имитирующая игру на электрогитаре.
        """
        return "Playing the electric guitar with a powerful, amplified sound..."

    def amplify(self) -> str:
        """
        Возвращает строку, имитирующую усиление звука электрогитары.

        Возвращает:
            str: Строка, имитирующая усиление звука электрогитары.
        """
        return "Amplifying the sound of the electric guitar..."

if __name__ == "__main__":
    # Пример использования классов
    acoustic = AcousticGuitar(brand="Taylor", model="214ce", price=999.99, serial_number="T12345", wood_type="Mahogany")
    electric = ElectricGuitar(brand="Fender", model="Stratocaster", price=1499.99, serial_number="F67890", pickup_type="Single Coil")

    print(acoustic)
    print(repr(acoustic))
    print(acoustic.play())

    print(electric)
    print(repr(electric))
    print(electric.play())
    print(electric.amplify())
