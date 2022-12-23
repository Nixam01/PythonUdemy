for number in range(20):
    print(number)


for number in range(1,21):
    print(number)

for number in range(1,21, 3):
    print(number)

for number in range(1,21):
    if number %2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))


#zadania

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for string in range (10):
    print(string_A)

print('\n\n')


for index in range (1,10):
    if index %2 == 0:
        print(string_B)
    else:
        print(string_A)

count = 1
for index in range (9):
    print('x'*count)
    count += 1

count = 1
for index in range (1, 10):
    if index %2 == 1:
        print('o'*count)
    else:
        print('x'*count)
    count +=1