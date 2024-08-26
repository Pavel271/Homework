class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        self.new_floor = new_floor
        if self.new_floor < 1 or self.new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for self.new_floor in range(1, new_floor + 1):
                print(self.new_floor)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)