# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class FishingRod:
    """
       Инициализация удочки.

       Args:
           throw_force (int): Сила заброса удочки (от 5 до 100).
           rarity_fishing_rod (int): Редкость удочки (от 1 до 5).
    """

    def __init__(self, throw_force: int, rarity_fishing_rod: int):

        if not isinstance(throw_force, int):
            raise TypeError
        if not (5 <= throw_force <= 100):
            raise ValueError

        if not isinstance(rarity_fishing_rod, int):
            raise TypeError
        if not (1 <= rarity_fishing_rod <= 5):
            raise ValueError

        self.throw_force = throw_force
        self.rarity_fishing_rod = rarity_fishing_rod

    def cast(self) -> int:
        """
        Забросить удочку

         Returns:
            int: Сила заброса удочки.

        >>> rod = FishingRod(50, 3)
        >>> rod.cast()
        40
        """
        return self.throw_force

    def reel_in(self) -> str:
        """
        Вытянуть рыбу

        Returns:
            str: Сообщение о вытягивании рыбы.

        >>> rod = FishingRod(50, 3)
        >>> rod.reel_in()
        'Вы вытянули рыбу'
        """
        ...

class Lake:
    """
    Инициализация озера.

    Args:
        square (int): Площадь озера (не менее 7 км^2).
        depth (int): Глубина озера (не менее 1 метра).
    """

    def __init__(self, square: int, depth: int):

        if not isinstance(square, int):
            raise TypeError
        if not (7 <= square):
            raise ValueError

        if not isinstance(depth, int):
            raise TypeError
        if not (1 <= depth):
            raise ValueError

        self.square = square
        self.depth = depth

    def random_spawn_fish(self) -> int:
        """
        Добавлят в озеро рыбу, расчитывая ее кол-во из площади и глубины.

        Returns:
            int: Количество рыбы в озере.

        >>> lake = Lake(100, 5)
        >>> lake.random_spawn_fish()
        49
        """
        fish_count = (self.square * self.depth) // 10
        return fish_count

    def calculate_volume(self) -> int:
        """
        Расчитывает объем озера

        Returns:
            int: Объем озера в кубических единицах.

        >>> lake = Lake(100,5)
        >>> lake.calculate_volume()
        500
        """
        return self.square * self.depth

class Boat:

    """
    Инициализация лодки.

    Args:
        number_of_seats (int): Количество мест в лодке (от 1 до 4).
        speed (int): Скорость лодки (не более 20 км/ч).
    """

    def __init__(self, number_of_seats: int, speed: int):

        if not isinstance(number_of_seats, int):
            raise TypeError
        if not (1 <= number_of_seats <= 4):
            raise ValueError

        if not isinstance(speed, int):
            raise TypeError
        if not (speed <= 20):
            raise ValueError
        self.number_of_seats = number_of_seats
        self.speed = speed

    def start_engine(self) -> str:
        """
        Завести двигатель

        Returns:
            str: Сообщение о запуске двигателя.

        >>> boat = Boat(4, 20)
        >>> boat.stop_engine()
        'Двигатель заведен'
        """
        ...

    def stop_engine(self) -> str:
        """
        Заглушить двигатель

        Returns:
            str: Сообщение о заглушении двигателя

        >>> boat = Boat(4, 20)
        >>> boat.stop_engine()
        'Двигатель заглушен'
        """
        ...
# TODO работоспособность экземпляров класса проверить с помощью doctest

if __name__ == "__main__":
    doctest.testmod()
