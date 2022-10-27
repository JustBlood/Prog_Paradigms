from abc import ABCMeta, abstractmethod
import copy

"""
Прототипное программирование:
Модель-прототип обеспечивает независимость от конкретного класса. Мы можем реализовать новый объект независимо от существующего класса.
Это также полезно для решения повторяющихся и сложных проблем разработки программного обеспечения.
"""
# класс, реализующий основные методы для будущих наследников,
# для реализации хеширования в функциях и классах ниже
class Courses_JTP(metaclass=ABCMeta):

    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


# Конкретные классы - курсы в университете, которые наследуют от общего родителя Courses_JTP

class Python(Courses_JTP):
    """ Class for Data Structures and Algorithms"""
    def __init__(self):
        super().__init__()
        self.type = "Python Basic and Algorithm"

    def course(self):
        print(" Inside Python :: course() method ")


# Курс по Java
class Java(Courses_JTP):
    # Class for Java langauge"""
    def __init__(self):
        super().__init__()
        self.type = "Java Basics and Spring Boot"

    def course(self):
        print(" Inside Java :: course() method. ")



# Курс по "R"
class R(Courses_JTP):
    # Class for R langauge"""
    def __init__(self):
        super().__init__()
        self.type = "R programming language"

    def course(self):
        print(" Inside R :: course() method. ")

    # class - Courses At GeeksforGeeks Cache


class Courses_Cache:
    # словарь cache для связывания индекса курса с объектом курса.
    cache = {}

    # функция get_course возвращает экземпляр нужного класса по кешу.
    @staticmethod
    def get_course(sid):
        COURSE = Courses_Cache.cache.get(sid, None)
        return COURSE.clone()

    # функция load записывает в словарь cache пары вида ("хеш": Объект)
    @staticmethod
    def load():
        Python_c = Python()
        Python_c.set_id("1")
        Courses_Cache.cache[Python_c.get_id()] = Python_c

        Java_c = Java()
        Java_c.set_id("2")
        Courses_Cache.cache[Java_c.get_id()] = Java_c

        R_c = R()
        R_c.set_id("3")
        Courses_Cache.cache[R_c.get_id()] = R_c



# Основная функция.
if __name__ == '__main__':
    # подгружаются все кеши для определенный классов для возможности их копирования
    Courses_Cache.load()

    # Новый объект создается не объявлением нового экземпляра класса Python()(также для Java(), R() и др.),
    # а с помощью копирования уже существующего класса из кеша-функции с помощью кеша.
    Python1 = Courses_Cache.get_course("1")
    print(Python1.get_type())

    Java2 = Courses_Cache.get_course("2")
    print(Java2.course())
    java3 = Courses_Cache.get_course("2")
    java4 = Courses_Cache.get_course("2")
    java5 = Courses_Cache.get_course("2")
    java6 = Courses_Cache.get_course("2")
    java7 = Courses_Cache.get_course("2")
    print(id(java3),
          id(java4),
          id(java5),
          id(java6),
          id(java7),
          "Как можем заметить - все ID РАЗНЫЕ! => объекты копируются корректно",
          sep=', ')

    R3 = Courses_Cache.get_course("3")
    print(R3.get_type())