import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies_power = 100
        number_days = 0
        print(f'{self.name}, на нас напали!')
        while enemies_power > 0:
            enemies_power -= self.power
            number_days += 1
            print(f'{self.name} сражается {number_days} дней(дня), осталось {enemies_power} воинов.')
            time.sleep(1)
            if enemies_power == 0:
                print(f'{self.name} одержал победу спустя {number_days} дней(дня)!' )

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')