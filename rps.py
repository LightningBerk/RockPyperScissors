import requests
import json
import random
rps = requests.get('https://rps101.pythonanywhere.com/api/v1/objects/all').text
rps = rps.replace("[", "")
rps = rps.replace("]", "")
rps = rps.replace("'", "")
rps = rps.split(",")
lst = []
for word in rps:
    lst.append(word)

player1 = ""
player2 = ""


def chooseRandom():
    player1 = lst[random.randint(0, len(lst))].strip('\"')
    player2 = lst[random.randint(0, len(lst))].strip('\"')
    print("Player One's choice is " + player1)
    print("Player Two's choice is " + player2)
    return player1, player2


def fightResult(x, y):
    x, y = chooseRandom()
    fightResult = requests.get(
        'https://rps101.pythonanywhere.com/api/v1/match?object_one=' + x + '&object_two=' + y)
    result = fightResult.json()
    winner = result['winner']
    loser = result['loser']
    outcome = result['outcome']
    print(winner + " " + outcome + " " + loser)


fightResult(player1, player2)
