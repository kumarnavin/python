import numpy as np


hh = int(input("Enter hour: "))
mi = int(input("Enter minutes: "))

print(hh, mi)
hour_angle = (360 * (hh%12)/12) + (360 /12) * (mi / 60)
min_angle = (360 * mi/60)
print(hour_angle, min_angle)
calc = abs(hour_angle - min_angle)
print("calc", calc)

actual=abs(30*hh - 5.5*mi)
print("actual", actual)
print("actual + calc", actual + calc)
