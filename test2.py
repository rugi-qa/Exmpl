import random as rnd
class Booking:
    list_id = []
    def __init__(self, name, amount_position):
        self.name = name
        self.amount_position = amount_position
        self.spot_list = []
        for i in range(amount_position):
            self.spot_list.append(i+1)
        self.residentId_list = []
        self.book_dict = {}

    def bookIt(self, spot_number):
        if spot_number not in self.spot_list:
            print('Такого номера нет в базе')
        else:
            if spot_number in self.book_dict.values():
                print('Номер занят!')
            else:
                print('Вы успешно забронировали номер!')
                residentId = rnd.randint(1000, 9999)
                while residentId in self.list_id:
                    residentId = rnd.randint(1000, 9999)
                self.list_id.append(residentId)
                self.residentId_list.append(residentId)
                self.book_dict.update({residentId: spot_number})

myHost1 = Booking('Гостинка 1', 10)
myHost2 = Booking('Гостинка 2', 7)
print(myHost1.spot_list)
print(myHost2.spot_list)
myHost1.bookIt(0)
myHost1.bookIt(1)
myHost1.bookIt(4)
myHost1.bookIt(4)
print(myHost1.book_dict)
