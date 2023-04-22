import aiogram as aio
import random as rnd
from modules.RPS import RPS

rock = RPS.GameItem('Камень', 0, 2, 1)
paper = RPS.GameItem('Бумага', 1, 0, 2)
scissors = RPS.GameItem('Ножницы', 2, 1, 0)

handGame = RPS.handItem(rock, scissors, paper)

phrase_tuple = ("Что бы это значило?", "Извини, такого я не понимаю...", "Это какой-то текст... Хотел бы я знать, что он значит :(", "Когда-то и меня вела дорога приключений...")

with open('privacy/tokenBot.txt', 'r') as tokenBot_file:
    thisBotToken = tokenBot_file.read()
thisBot = aio.Bot(thisBotToken)

dp = aio.Dispatcher(thisBot)
flagRSP = 'False'
flagEcho = 'False'

with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
    flagRSP_file.write(str(flagRSP))

with open('cache/flag_echo.txt', 'w') as flagEcho_file:
    flagEcho_file.write(str(flagEcho))


@dp.message_handler(commands=["start"])
async def process_start_command(message: aio.types.Message):
    await message.reply("Привет!\nЯ на связи и жду команды!\nНапиши /help и я расскажу, что умею :)")

@dp.message_handler(commands=["help"])
async def process_help_command(message: aio.types.Message):
    await message.reply("/help - список команд \n/echo - эхо-бот \n/RSP - камень-ножницы-бумага")

@dp.message_handler(commands=["echo"])
async def echo_bot(message: aio.types.Message):
    await message.reply("Играем в эхо!\nНапиши /echostop, если захочешь закончить!")
    flagEcho = "True"
    with open('cache/flag_echo.txt', 'w') as flagEcho_file:
        flagEcho_file.write(str(flagEcho))


@dp.message_handler(commands=["RSP"])
async def echo_bot(message: aio.types.Message):
    await message.reply("Играем в камень-ножницы-бумага!\nНапиши /RSPstop, чтобы закончить!")
    flagRSP = "True"
    with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
        flagRSP_file.write(str(flagRSP))


@dp.message_handler(commands=["Rock"])
async def choose_rock(message: aio.types.Message):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        playerTurn = handGame.choise(True, 1)
        PCTurn = handGame.choise(False, 1)
        result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
        await thisBot.send_message(
            message.from_user.id,
            text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
        )

@dp.message_handler(commands=["Scissors"])
async def choose_scissors(message: aio.types.Message):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        playerTurn = handGame.choise(True, 2)
        PCTurn = handGame.choise(False, 2)
        result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
        await thisBot.send_message(
            message.from_user.id,
            text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
        )

@dp.message_handler(commands=["Paper"])
async def choose_paper(message: aio.types.Message):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        playerTurn = handGame.choise(True, 3)
        PCTurn = handGame.choise(False, 3)
        result_msg = RPS.compareHand(playerTurn['Game_Item'], PCTurn['Game_Item'])
        await thisBot.send_message(
            message.from_user.id,
            text=f'{playerTurn["msg"]},\n{PCTurn["msg"]},\n{result_msg}',
        )

@dp.message_handler()
async def get_text_from_messages(message: aio.types.Message):
    with open('cache/flag_echo.txt', 'r') as flagEcho_file:
        flagEcho = flagEcho_file.read()
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == "False":
        if flagEcho == "True":
            if message.text != '/echostop':
                await thisBot.send_message(message.from_user.id, f'Все говорят "{message.text}", а ты купи слона')
                flagEcho = "True"
            elif message.text == '/echostop':
                await thisBot.send_message(message.from_user.id, 'Не играем в эхо!')
                flagEcho = "False"
        else:
            flagEcho = "False"
            await message.reply(rnd.choice(phrase_tuple))
        with open('cache/flag_echo.txt', 'w') as flagEcho_file:
            flagEcho_file.write(str(flagEcho))

    else:
        if message.text == '/RSPstop':
            await thisBot.send_message(message.from_user.id, 'Не играем в камень-ножницы-бумага!')
            flagRSP = "False"
            with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
                flagRSP_file.write(str(flagRSP))

aio.executor.start_polling(dp)
