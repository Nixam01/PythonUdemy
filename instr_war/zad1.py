age = 23
if age >= 18:
    print("You can buy alco")
else:
    print("You are too young to buy alcohol")

likes = 500
minshares = 100

numlikes = 1300
shares = 55


if (numlikes > likes and shares > minshares):
    print("PROMOCJA ---> Cena została obniżona o 10%")
else:
    print("NOT ENOUGH VALUES")

isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = False
if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("THERE IS A FREE COUPON")
else:
    print("CONTINUE YOUR SHOPPING")

itRains = True
if itRains:
    print("We stay at home")
else:
    print("we go out")

print("we stay at home" if itRains else "we got out")

#zadania

musclePain = False
fever = True
weakness = True
print("Suspicion of influenza" if musclePain and fever and weakness else "The flu is unlikely")

