#for i in range(32, 127):
#    print(i, chr(i))

ints = range(33, 127)
password = ''

import random
for i  in range (8):
    password += chr(random.randint(33, 127))

print("password is:", password)


import random
min = 1
max = 6
dice = random.choice(range(min, max))
if dice == 1:
    print('\n', ' o ', '\n')
elif dice == 2:
    print('  o', '\n', '\n', 'o  ')
elif dice == 3:
    print(' o\n', ' o ', '\no  ')
elif dice == 4:
    print('o o\n', '\no o')
elif dice == 5:
    print('o o\n', 'o', '\no o')
elif dice == 6:
    print('o o', '\n', 'o o', '\n', 'o o')

dices = []
for j in range(5):
    dices.append(random.choice(range(min, max)))

dices.sort()
print(dices)