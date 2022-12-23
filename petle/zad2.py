values=[10, 43, 12, 48, 12, 11, 18, 98, 57, 28,  19, 27, 49, 19, 74]

i = 0
max = len(values)-2

while i<max:
    if values[i]<values[i+1] and values[i+1]<values[i+2]:
        print('Found:' ,values[i], values[i+1], values[i+2])
    i+=1


#zadanka

print('Task 2 \n')

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i=0
max = len(numbers)-1

while i<max:
    if numbers[i+1] == numbers[i]**2:
        print('Found:', numbers[i+1], numbers[i])
    i+=1


i=0
max = len(numbers)-2

print('--------------')

while i<max:
    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2==numbers[i+2]:
        print('Found: ', numbers[i], numbers[i+1],numbers[i+2])
    i+=1


print('----zad3----')

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

i = 0
max = len(texts)-1

while i<max:
    if len(texts[i]) == len(texts[i+1]):
        print('Found: ', texts[i], texts[i+1])
    i+=1


