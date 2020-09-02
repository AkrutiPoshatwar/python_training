from datetime import date
from datetime import timedelta

d1 = date(2020, 9, 1)
i=0
while i < 5:
    day = [d1 + timedelta(days = 5)]
    d1 = d1 + timedelta(days=5)
    i+=1

    print(day)