number = [1]
width = 60
height = 10

line = ''
for n in number:
    line+= "%3d " % (n)
print(line.center(width))

for i in range(height-1):
    newNumbers = [1]
    position = 0
    while position < len(number) -1:
        newNumbers.append(number[position] + number[position+1])
        position+=1
    newNumbers.append(1)
    number = newNumbers.copy()
    line = ''
    for n in number:
        line += "%3d " % (n)
    print(line.center(width))

