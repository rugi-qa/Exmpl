import random as rnd

class GameItem:
    def __init__(self, name, *power):
        self.name = name
        self.power = list(power)

class handItem:
    def __init__(self, *gameItem):       
        self.gameItem = list(gameItem)

    def choise_msg(self):
        print()
        print('Сделайте выбор:')
        print()
        for i in range(len(self.gameItem)):
            print(f'{i + 1} {self.gameItem[i].name}')
        return int(input())

    def choise(self, thisPlayer, thisChoise):
        result_dict = dict()
        this_msg = ''
        self.thisPlayer = thisPlayer
        if self.thisPlayer == True:
            __myChoise = thisChoise
            print()
            print(f'Игрок выбрал: {self.gameItem[__myChoise -1].name}')
            this_msg = f'Игрок выбрал: {self.gameItem[__myChoise -1].name}'
        else:
            __myChoise = rnd.randint(1,len(self.gameItem))
            print()
            print(f'Бот выбрал: {self.gameItem[__myChoise -1].name}')
            this_msg = f'Бот выбрал: {self.gameItem[__myChoise -1].name}'

        result_dict['Game_Item'] = self.gameItem[__myChoise -1]
        result_dict['msg'] = this_msg
        return result_dict

def compareHand(playerHand, PCHand):
    print()
    text_result = ''
    if playerHand.name == PCHand.name:
        text_result = 'Ничья!'
    else:
        winCounter = 0
        for i in range(len(playerHand.power)):
            if playerHand.power[i] > PCHand.power[i]:
                winCounter +=1
        if winCounter > len(playerHand.power) / 2:
            text_result = 'Игрок победил!'
        else:
            text_result = 'Бот победил!'
    print(text_result)
    print()
    return text_result

stone = GameItem('Камень', 0, 2, 1)
paper = GameItem('Бумага', 1, 0, 2)
scissors = GameItem('Ножницы', 2, 1, 0)

handGame = handItem(stone, scissors, paper)

while True:


    playerTurn = handGame.choise(True, handGame.choise_msg())
    # print(playerTurn['Game_Item'])
    PCTurn = handGame.choise(False, 1)
    compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
    print('****')
