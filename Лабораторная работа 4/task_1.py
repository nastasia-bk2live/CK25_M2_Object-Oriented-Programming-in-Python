from typing import Union


class Building:
    """
    Базовый класс, описывающий здание.

    Содержит основные характеристики:
    - название здания
    - высоту
    - площадь
    """

    def __init__(self, name: str, height: Union[int, float], area: Union[int, float]) -> None:
        """
        Создает объект здания

        :param name: название здания
        :param height: высота здания (м)
        :param area: площадь здания (м2)

        Примеры:
            >>> building = Building("Бизнес центр", 40, 8000)
        """

        if not isinstance(name, str):
            raise TypeError("Название здания должно быть строкой")

        if not name.strip():
            raise ValueError("Название здания не может быть пустым")

        self._name = name.strip()

        self.height = height
        self.area = area

    @property
    def name(self) -> str:
        """
        Название здания

        Примеры:
            >>> building = Building("Торговый центр", 35, 6000)
            >>> building.name
            'Торговый центр'
        """
        return self._name

    @property
    def height(self) -> Union[int, float]:
        """Высота здания"""
        return self._height

    @height.setter
    def height(self, value: Union[int, float]) -> None:
        """Устанавливает высоту здания"""
        if not isinstance(value, (int, float)):
            raise TypeError("Высота должна быть числом")

        if value <= 0:
            raise ValueError("Высота должна быть больше нуля")

        self._height = value

    @property
    def area(self) -> Union[int, float]:
        """Площадь здания"""
        return self._area

    @area.setter
    def area(self, value: Union[int, float]) -> None:
        """Устанавливает площадь здания"""
        if not isinstance(value, (int, float)):
            raise TypeError("Площадь должна быть числом")

        if value <= 0:
            raise ValueError("Площадь должна быть больше нуля")

        self._area = value

    def calculate_volume(self) -> float:
        """
        Рассчитывает приблизительный объем здания

        Примеры:
            >>> building = Building("Склад", 10, 2000)
            >>> building.calculate_volume()
        """
        return self.area * self.height

    def __str__(self) -> str:
        """
        Строковое описание здания

        Примеры:
            >>> building = Building("Офис", 25, 3000)
            >>> print(building)
        """
        return f"Здание '{self.name}', высота {self.height} м, площадь {self.area} м²"

    def __repr__(self) -> str:
        """
        Представление объекта для разработчика

        Примеры:
            >>> building = Building("Офис", 25, 3000)
            >>> repr(building)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, height={self.height}, area={self.area})"


class ResidentialBuilding(Building):
    """
    Класс жилого здания

    Дополнительно хранит количество квартир
    """

    def __init__(self, name: str, height: Union[int, float], area: Union[int, float], apartments: int) -> None:
        """
        Создает жилое здание

        :param apartments: количество квартир

        Примеры:
            >>> house = ResidentialBuilding("ЖК Северный", 55, 18000, 300)
        """

        super().__init__(name, height, area)

        if not isinstance(apartments, int):
            raise TypeError("Количество квартир должно быть целым числом")

        if apartments <= 0:
            raise ValueError("Количество квартир должно быть положительным")

        self._apartments = apartments

    @property
    def apartments(self) -> int:
        """
        Количество квартир

        Примеры:
            >>> house = ResidentialBuilding("ЖК Восточный", 50, 16000, 200)
            >>> house.apartments
            200
        """
        return self._apartments

    def calculate_volume(self) -> float:
        """
        Перегруженный метод расчета объема

        Причина перегрузки:
        для жилых зданий расчет объема может отличаться,
        так как учитываются жилые этажи и внутренние помещения
        """
        return super().calculate_volume() * 0.9


class IndustrialBuilding(Building):
    """
    Класс промышленного здания

    Используется для описания складов и производственных помещений
    """

    def __init__(self, name: str, height: Union[int, float], area: Union[int, float], purpose: str) -> None:
        """
        Создает промышленное здание

        :param purpose: назначение здания

        Примеры:
            >>> factory = IndustrialBuilding("Заводской корпус", 25, 9000, "Машиностроительный цех")
        """

        super().__init__(name, height, area)

        if not isinstance(purpose, str):
            raise TypeError("Назначение должно быть строкой")

        if not purpose.strip():
            raise ValueError("Назначение не может быть пустым")

        self._purpose = purpose.strip()

    @property
    def purpose(self) -> str:
        """
        Назначение здания

        Примеры:
            >>> factory = IndustrialBuilding("Склад", 15, 4000, "Логистический центр")
            >>> factory.purpose
            'логистический центр'
        """
        return self._purpose

    def get_building_type(self) -> str:
        """
        Возвращает описание типа здания

        Примеры:
            >>> factory = IndustrialBuilding("Склад", 15, 4000, "Логистический центр")
            >>> factory.get_building_type()
        """
        return f"Промышленное здание: {self.purpose}"