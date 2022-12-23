number = [1]
print(number)

for i in range(5):
    newNumbers = [1]
    position = 0
    while position < len(number) -1:
        newNumbers.append(number[position] + number[position+1])
        position+=1
    newNumbers.append(1)
    number = newNumbers.copy()
    print(number)


colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []
for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard['Color'] = color
        allCards.append(aCard)


import random
random.shuffle(allCards)
print(allCards)


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

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 2--------')
print(player2)

'''' while len(player1)>0 and len(player2)>0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1['Power'] == card2['Power']:
        player1.append(card1)
        player2.append(card2)
    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
    elif card1['Power'] < card2['Power']:
        player2.append(card2)
        player2.append(card1)


if len(player1)>0:
    print('gracz 1 wygrał wojne')
else:
    print('gracz 2 wygrał wojne')

'''

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        # print('=EQUAL \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        # print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    else:
        player2.append(card2)
        player2.append(card1)
        # print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')

if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')
