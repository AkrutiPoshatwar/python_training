from datetime import date
from datetime import timedelta

d1 = date(2020, 9, 1)
d2 = date(2020, 9, 30)
day = []

for x in range(1, 30, 5):
    day.append([d1 + timedelta(days=5)])
    d1 = d1 + timedelta(days=5)

print(day)