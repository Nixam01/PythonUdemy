countries = ['FR', 'US', 'DE', 'RU']
countries[1] = 'GB'
countries.append('PL')
countries.insert(2, 'ES')
countries.sort()
countries.reverse()
print(countries.pop(2)) #wypisuje i wyrzuca element z listy
print(countries[1])
print(countries)
print(countries.index('PL')) #wypisuje miejsce danego elementu w liście
print(countries.count('DE')) #ile razy dana wartość pojawia się w liście

newList = ['FI', 'SE']
countries.extend(newList)
print(countries)
countriesCopy = countries.copy()
countriesCopy.clear()
print(countries)
print(countriesCopy)

#zadania

list1 = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']
print(list1)
list1.append('CHILD IN TIME')
print(list1)
print('\n')
list1.append('AGAIN')
print(list1)
print('\n')
list1.insert(2, 'HOTEL CALIFORNIA')
print(list1)
print('\n')
list1.insert(0, 'THE SOUND OF SILENCE')
print(list1)
print('\n')
print(list1.index('HOTEL CALIFORNIA')+1)
list1.pop(3)
print(list1)
print('\n')
list1.pop(0)

list1.insert(0, 'ENJOY THE SILENCE')
print(list1)
print('\n')
hitsToRead = list1.copy()
hitsToRead.reverse()
print(hitsToRead)
hitsToRead.sort()
print(hitsToRead)
print(hitsToRead)
print(hitsToRead.pop(0))
print(hitsToRead.pop(1))
additionalSongs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead)
print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))
hitsToRead.clear()

