import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
#Жилая комната в общежитии
class DormRoom:
    def __init__(self, room_number: int, residents_count: int, gender: str):
        """
        Создание объекта "Жилая комната в общежитии"

        :param room_number: Номер комнаты
        :param residents_count: Количество проживающих (1–4)
        :param gender: Пол проживающих ("male" или "female")

        Примеры:
        >>> room = DormRoom(101, 2, "female")
        """
        if not isinstance(room_number, int):
            raise TypeError("Номер комнаты должен быть целым числом")

        if not isinstance(residents_count, int):
            raise TypeError("Количество проживающих должно быть целым числом")
        if not 1 <= residents_count <= 4:
            raise ValueError("В комнате может проживать от 1 до 4 человек")

        if gender not in ("male", "female"):
            raise ValueError("Пол должен быть 'male' или 'female'")

        self.room_number = room_number
        self.residents_count = residents_count
        self.gender = gender

    def add_resident(self) -> None:
        """
        Добавление одного проживающего в комнату.

        :raise ValueError: Если превышен лимит проживающих

        Примеры:
        >>> room = DormRoom(102, 3, "male")
        >>> room.add_resident()
        """
        ...

    def remove_resident(self) -> None:
        """
        Выселение одного проживающего из комнаты.

        :raise ValueError: Если в комнате уже минимальное количество жильцов

        Примеры:
        >>> room = DormRoom(103, 1, "female")
        >>> room.remove_resident()
        """
        ...

    def is_full(self) -> bool:
        """
        Проверка, заполнена ли комната полностью.

        :return: True, если в комнате 4 человека

        Примеры:
        >>> room = DormRoom(104, 4, "male")
        >>> room.is_full()
        """
        ...


#Учебная группа на курсе
class StudyGroup:
    def __init__(self, group_name: str, students_count: int):
        """
        Создание объекта "Учебная группа"

        :param group_name: Номер группы
        :param students_count: Количество студентов (не более 30)

        Примеры:
        >>> group = StudyGroup("3150801/10102", 27)
        """
        if not isinstance(group_name, str):
            raise TypeError("Номер группы должно быть строкой")

        if not isinstance(students_count, int):
            raise TypeError("Количество студентов должно быть целым числом")
        if students_count < 0 or students_count > 30:
            raise ValueError("В группе может быть от 0 до 30 студентов")

        self.group_name = group_name
        self.students_count = students_count

    def add_student(self) -> None:
        """
        Добавление студента в группу.

        :raise ValueError: Если группа переполнена

        Примеры:
        >>> group = StudyGroup("3150801/10101", 30)
        >>> group.add_student()
        """
        ...

    def remove_student(self) -> None:
        """
        Удаление студента из группы.

        :raise ValueError: Если в группе нет студентов

        Примеры:
        >>> group = StudyGroup("3150801/10101", 1)
        >>> group.remove_student()
        """
        ...

    def is_full(self) -> bool:
        """
        Проверка, заполнена ли группа.

        :return: True, если в группе 30 студентов

        Примеры:
        >>> group = StudyGroup("3150801/10101", 30)
        >>> group.is_full()
        """
        ...


#Склад для хранения
class Warehouse:
    def __init__(self, capacity: int, occupied: int):
        """
        Создание объекта "Склад"

        :param capacity: Максимальная вместимость склада
        :param occupied: Занятый объём

        Примеры:
        >>> warehouse = Warehouse(1000, 200)
        """
        if not isinstance(capacity, int):
            raise TypeError("Вместимость склада должна быть целым числом")
        if capacity <= 0:
            raise ValueError("Вместимость склада должна быть положительной")

        if not isinstance(occupied, int):
            raise TypeError("Занятый объём должен быть целым числом")
        if occupied < 0 or occupied > capacity:
            raise ValueError("Занятый объём не может превышать вместимость")

        self.capacity = capacity
        self.occupied = occupied

    def add_goods(self, amount: int) -> None:
        """
        Добавление товара на склад.

        :param amount: Количество добавляемого товара
        :raise ValueError: Если превышена вместимость склада

        Примеры:
        >>> warehouse = Warehouse(500, 100)
        >>> warehouse.add_goods(200)
        """
        if not isinstance(amount, int):
            raise TypeError("Количество товара должно быть целым числом")
        if amount <= 0:
            raise ValueError("Количество товара должно быть положительным")
        ...

    def remove_goods(self, amount: int) -> None:
        """
        Удаление товара со склада.

        :param amount: Количество удаляемого товара
        :raise ValueError: Если товара недостаточно

        Примеры:
        >>> warehouse = Warehouse(500, 300)
        >>> warehouse.remove_goods(100)
        """
        ...

    def free_space(self) -> int:
        """
        Определение свободного места на складе.

        :return: Свободная вместимость склада

        Примеры:
        >>> warehouse = Warehouse(500, 200)
        >>> warehouse.free_space()
        """
        ...


if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
