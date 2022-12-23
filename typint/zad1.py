print(type(5/3))
import sys
print(sys.maxsize)
print(5//3)
print(5%3)

#zadania

name = "Marcin"
age = 21
daysInYear = 365
message = name + ' is ' + str(age)+  ' years old, so is about '+ str(daysInYear*age) +' days old'
print(message)
name = "Karol"
age = 50
message = name + ' is ' + str(age)+  ' years old, so is about '+ str(daysInYear*age) +' days old'
print(message)

message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name, age, daysInYear*age))

name = "Chris"
age = 17
print(message.format(name, age, daysInYear*age))

print(1234567890%12345)
