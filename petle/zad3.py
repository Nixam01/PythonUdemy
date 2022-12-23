cargo = [40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
cargo.sort()
cargo.reverse()

boxCapacity = 90
box = []
i = 0

#and boxCapacity - sum(box) >= min(cargo)

while i<len(cargo):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print("the collected items sum is:", sum(box))
print("the elements are:",box, "\n")

print("druga wersja \n")

# zadanka

number = 1
previousnumber  = 0
while number <= 50:
    print("sum of numbers: ", number+previousnumber)
    previousnumber += 1
    number += 1

# zad 2

import random

my_number = random.randint(0,20)

guess = -1
print("Guess my number")
trials = 0;

while guess != my_number:
    guess = int(input())
    trials += 1
    if(my_number == guess):
        print("You've guessed, congrats bro!")
        print("number of tries", trials, "\n")
    if (my_number != guess):
        print("try again bruhhhh xDDD")






