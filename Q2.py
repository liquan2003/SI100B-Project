#Question 2

import math
grd = 0.0
loc = 0.0
si = 0.0 

for i in range(55):
    grd = float(input())
    loc = loc + grd / 55
print(loc)
for i in range(55):
    grd = float(input())
    si = si + (grd - loc)*(grd - loc) / 55
si = math.sqrt(si)
print(si)
l = loc - 2 * si 
r = loc + 2 * si
print("(",l,",",r,")")
