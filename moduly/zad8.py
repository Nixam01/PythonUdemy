import random

myNumbers  = []

while len(myNumbers) < 7:
    newNumber = random.randint(1, 49)
    if newNumber in myNumbers:
        print("eliminated: ", newNumber)
        continue
    myNumbers.append(newNumber)
print("Those numbers will win:", myNumbers)


colors = ['Kier','Karo','Trefl','Pik']
figures = ['Ace','King','Queen','Jack','10','9']

allCards = []
for color in colors:
    for figure in figures:
        allCards.append(color + " "+ figure)


print(allCards)

random.shuffle(allCards)
player1 = []
player2 = []

max = len(allCards)
i = 0
while i < max-1:
    if i%2 == 0:
        player1.append(allCards[i])

    else:
        player2.append(allCards[i])
    i+=1

print('player 1 cards: ', player1, '\nplayer 2 cards', player2)