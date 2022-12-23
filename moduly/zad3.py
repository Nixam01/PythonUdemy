import random
for liczba in range(1,10):
    print(random.randint(1,100))

number1 = random.randint(1,100)
counter = 1
number2 = 0
while number2 != number1:
    number2 = random.randint(1,100)
    counter += 1
    print("counter: ", counter , '\n')
    print(number2)
print('ilość wszystkich prób', counter)
print(number1)

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
random.shuffle(countries)
groupNumber = 0
for country in countries:
    if countries.index(country)%4 ==0:
        groupNumber += 1
        print('-----Grupa %d-----'%(groupNumber))
    print(country)
