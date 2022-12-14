# importing modules
import requests
import json
import random
import os

# formatting api return data
rps = requests.get('https://rps101.pythonanywhere.com/api/v1/objects/all').text # grabs list of all the rock paper scissors objects

char_remove = ["[", "]", "'"] # list of characters to remove from the returned text
for char in char_remove:  # scrubs through the string and removes the listed characters
    rps = rps.replace(char, "")

rps = rps.split(",")  # splits up the string into individual objects

lst = []
for word in rps:  # makes a list with all of your sperated objects
    lst.append(word)

# defining player 1 and 2 variables
player1 = ""
player2 = ""

# defining functions
def chooseRandom():
    # chooses a random object from the list for each player
    player1 = lst[random.randint(0, len(lst))].strip('\"')
    player2 = lst[random.randint(0, len(lst))].strip('\"')
    print("Player One's choice is " + player1 + "\nPlayer Two's choice is " + player2)
    return player1, player2

def fightResult(x, y):
    x, y = chooseRandom()  # passing through our random choices from chooseRandom()
    fightResult = requests.get(
        'https://rps101.pythonanywhere.com/api/v1/match?object_one=' + x + '&object_two=' + y)  # api call to return the result of the battle
    result = fightResult.json()  # json parsing of result
    winner = result['winner']
    loser = result['loser']
    outcome = result['outcome']
    print(winner + " " + outcome + " " + loser)  # output parsed result text

# main
try:
    while True:
        os.system("cls")
        fightResult(player1, player2)
        input("Press enter to battle again or Ctrl+C to exit!")
except KeyboardInterrupt:
    pass