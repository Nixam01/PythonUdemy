filename = 'c:\\temp\\output.txt'
line = 'Europe'
cities = ['London', 'Berlin', 'Paris']

file = open(filename, 'w')
file.write(line)
file.write('\n')

for city in cities:
    file.write(city)+file.write('\n')

file.close()