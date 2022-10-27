import time


class TrafficLight():

    # Определяем время ожидания сигнала светофора,
    # можно поместить __init__ для ручного ввода промежутков между сигналами
    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 4

    # Определяем названия цветов сигналов светофора
    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        # создаем приватную переменную, доступ к ней только у нас
        self.__color = color
        print(f'\nСоздан новый объект TrafficLight со стартовым цветом {self.__color}')

    def switch_light(self, color, wait_period):
        self.wait_period = wait_period
        print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
        time.sleep(self.wait_period)

    def running(self, color = ''):

        # Если при вызове метода цвет не указан, берем из родительского класса
        # В противном случае стартуем с цвета, объявленного при вызове метода
        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.switch_light('красный', self.red_color_wait)
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        elif loc_color == self.yellow_color_name:
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        else:
            self.switch_light('зеленый', self.green_color_wait)

        # Можно сделать бесконечный цикл для каждого из экземпляров,
        # но тогда не будет возможности показать работоспособность такой программы
        # при различных вариантах запуска и нач. значений
        print('Цикл переключения цветов завершен')

tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()

# Инициализируем класс красным цветом, а метод запускаем с желтого
tl1 = TrafficLight('красный')
tl1.running('желтый')