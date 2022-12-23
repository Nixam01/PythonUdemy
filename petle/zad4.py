data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for s in data:
    print(s.upper())

#zadanie 2


for s in data:

    elements = s.split(':')
    print(elements[0].upper())
    print(elements[1])



