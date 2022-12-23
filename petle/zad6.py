for x in range (1,10):
    for y in range (1,10) :
        print (x, y, x*y)

for x in range (1, 6):
    line = str(x)
    for y in range(1,6):
        line += '\t'+str(x*y)
    print(line)

#zadania
score = 1
i = 10
for x in range (1, i+1):
    score = score *x
print(score)


newscore = 1
for y in range (1, 11):
    newscore = newscore *y
    print(newscore)

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for element in list_noun:
    for adjective in list_adj:
        print(element, adjective)