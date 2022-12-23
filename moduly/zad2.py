percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

import math

percent.sort()
print(percent)



import statistics

print(statistics.median(percent))
print(statistics.median_low(percent))
print(statistics.median_high(percent))

print('\n')
import math

degree = 360
radianvalue = degree*math.pi/180
print(radianvalue)

degree = 45
radianvalue = degree*math.pi/180
print(radianvalue)

print(math.radians(360), math.radians(45))

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38
small_pizza_price = 11.5
big_pizza_price = 15.6
family_pizza_price = 22

print('\n', small_pizza_r**2*math.pi, '\n', big_pizza_r**2*math.pi, '\n', family_pizza_r**2*math.pi)
print('\n', small_pizza_r**2*math.pi/10000, '\n', big_pizza_r**2*math.pi/10000, '\n', family_pizza_r**2*math.pi/10000)



print('\n', 11.5/small_pizza_r**2*math.pi/10000, '\n', 15.6/big_pizza_r**2*math.pi/10000, '\n', 22/family_pizza_r**2*math.pi/10000)