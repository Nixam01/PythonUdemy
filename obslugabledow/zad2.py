import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsstr = input('How many persons are there in the team? ')
    persons = int(personsstr)

    tasksPerPerson = tasks / persons

except ValueError as e:
    print('Sorry - you need to enter an integer number:', e)

except ZeroDivisionError as e:
    print('Sorry - you cant enter value = 0', e)

else:
    print("Every person should have around ", tasksPerPerson, " tasks")
finally:
    print("code ended with/without errors")