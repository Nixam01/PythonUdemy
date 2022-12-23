'''
Ten skrypt policzy ile razy mrugamy okiem w czasie X lat.
Zakładamy że:
-liczba mrugnięć na minutę to 20
-liczba minut w godzinie to 60
-liczba godzin w dobie to 24
-liczba lat( czyli nasz X) 50
Uwaga: jezeli przyjąć że spimy 8 godzin nad dobę to liczba godzin na dobę
powinna wynosić 16
'''
#liczba mrugnięć okiem na minutę
blinksPerMin = 20
#liczba minut na godzine i liczba godzin w dobie
minInHour = 60
hoursInDay = 16
daysInYear = 365
#liczba lat
years = 50
#liczba mrugniec w ciagu X lat
print(blinksPerMin*minInHour*hoursInDay*daysInYear*years)

#definitionOfVariables
daysOfWorkPerMonth = 20
monthsInYear = 12
vacation = 26
yearsOfWOrk = 40
#result
print((daysOfWorkPerMonth * monthsInYear - vacation)*yearsOfWOrk)