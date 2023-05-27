class Food:

    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class Fridge:

    def __init__(self, volume):
        self.volume = volume
        self.fullness = 0
        self.food_list = []

    def putFood(self, food):
        print(f'Свободный объем: {self.volume - self.fullness}')
        print(f'Вы хотите положить: {food.name} объемом {food.volume}')
        if food.volume > self.volume - self.fullness:
            print('Для этого продукта в холодильнике нет места!')
        else:
            self.fullness += food.volume
            self.food_list.append(food)

    def takeFood(self, food_name):
        print(f'Вы хотите взять {food_name}')
        for i in self.food_list:
            if food_name == i.name:
                print(f'{food_name} есть в холодильнике')
                self.fullness -= i.volume
                self.food_list.remove(i)
                break
        else:
            print(f'{food_name} нет в холодильнике')

meat = Food(name = 'Мясо', volume = 3)
fish1 = Food('Рыба', 2)
eggs = Food('Яйца', 1)
fish2 = Food('Рыба', 2)
pizza = Food('Пицца', 3)
bread = Food('Хлеб', 2)

myFridge = Fridge(10)
print(myFridge.food_list)
myFridge.putFood(meat)
myFridge.putFood(fish1)
myFridge.putFood(eggs)
myFridge.putFood(fish2)
myFridge.putFood(pizza)
myFridge.putFood(bread)
myFridge.takeFood('Торт')
myFridge.takeFood('Рыба')
for i in myFridge.food_list:
    print(i.name)
