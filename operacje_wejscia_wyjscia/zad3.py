
with open("c:\\temp\\joke.txt", "r") as file:
    content = file.read()
    print(content)

with open("c:\\temp\\joke.txt", "r") as file:
    for line in file:
        print(line)

file_path  = "c:\\temp\\orders.csv"
with open(file_path) as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' % (order[0], order[1], order[2]))
        else:
            print("Line %s malformed!!!" % line)

print("Processing finished")


