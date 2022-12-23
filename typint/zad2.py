IsWeekend = True
print("Is weekend =", IsWeekend)
Temperature = 25
print("Temperature =", Temperature)
TodoList=''
IsHappy = IsWeekend and Temperature >= 20 and TodoList == ''
print("IsHappy =", IsHappy)

#zadania
isAutomaticMode = True
# is the level of day-lighr above 80%
is80PercentLight = True
# is the Sun ligthing directly into the driver's face
isDirectLight = False
# is it rainy, foggy or other weather conditions are present
isRainy = False

turnLightsOn = isAutomaticMode and (not is80PercentLight  or isDirectLight or isRainy)
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print("\n")

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = False
turnLightsOn = isAutomaticMode and (not is80PercentLight  or isDirectLight or isRainy)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print("\n")

isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = True
turnLightsOn = isAutomaticMode and (not is80PercentLight  or isDirectLight or isRainy)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print("\n")

isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True
turnLightsOn = isAutomaticMode and (not is80PercentLight  or isDirectLight or isRainy)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print("\n")
