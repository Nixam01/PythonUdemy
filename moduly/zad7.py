import datetime

print('Minimum and maximum', datetime.MINYEAR, datetime.MAXYEAR)

today = datetime.date.today()
print('Today is' ,today)

daysToPay = datetime.timedelta(7)
print("the bill should be paid till:", today+daysToPay)

endOfTheWorld = datetime.date.max
print(endOfTheWorld)

bornDate = datetime.date(2001, 4,  17)
print(today- bornDate)


print('now()\t', datetime.datetime.now())
print('today()\t', datetime.datetime.today())
print('weekday()\t', datetime.datetime.today().weekday())

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

import math

leninput = len(inputdata)
factinput = len(factortable)

print('\n')

print(leninput)
print(factinput)
if leninput == factinput:
    i = 0
    print('ok')
    while i < leninput:
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print('minvalue=', minvalue, 'maxvalue=', maxvalue)
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print(mininteger, "\t", inputdata[i], "\t", maxinteger)
        i += 1

elif leninput != factinput:
    print('inputdata and factortable need to have equal number of elements')



import random
j = 0
while j < leninput:
    minvalue = inputdata[j] - random.choice(range(0,1)) * inputdata[j]
    maxvalue = inputdata[j] + random.choice(range(0,1)) * inputdata[j]
    print('minvalue=', minvalue, 'maxvalue=', maxvalue)
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger, "\t", inputdata[j], "\t", maxinteger)
    j += 1

from datetime import datetime
print(datetime.today())
print(datetime.today().strftime("%Y-%m-%d"))