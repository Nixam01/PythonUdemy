CountryLeaders = {'PL': 'Duda', 'US': 'Trump'}
print(CountryLeaders['US'])

CountryLeaders['DE'] = 'Merkel'
print(CountryLeaders)

print(CountryLeaders.keys())
print(CountryLeaders.values())
print(CountryLeaders.items())

print(CountryLeaders.popitem())

print(CountryLeaders)

CountryLeaders.setdefault('FR', 'Macron')

print(CountryLeaders)

print(CountryLeaders.get('RU'))

NewLeaders = {'RU': 'Putin', 'DE': 'Scholz'}
print(NewLeaders)
CountryLeaders.update(NewLeaders)
print(CountryLeaders)

#zadania

canals = {'Google': 1480, 'Email': 300, 'Natural Traffic': 440, 'TV Spot': 700}
print(canals['Email'])
channelsUpdate = {'Natural Traffic': 520, 'News': 600}
canals.update(channelsUpdate)
print(canals)
canals.pop('Email')
print(canals)