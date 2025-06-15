# To work with datetime module in python
import datetime as dt

#  to make a datetime object
d = dt.date(2016, 8, 12)
print(d)

#  to get todays date
tday = dt.date.today()
print(tday)

# to get year , month and day of a date
print(tday.year)
print(tday.month)
print(tday.day)

# weekday gives which week it is monday - 0 and isoweekday makes monday -1 and sunday -7
print(tday.weekday())

# timedeltas gives us differet times
t_delta = dt.timedelta(days= 7)
# Below gives us date after 7 days and date prior 7 days
print(tday+t_delta)
print(tday-t_delta)

# date_1+date_2 = time_delta
# date_1 + time_delta = date_2

# let's say i want to know how many days past my bday
bday = dt.date(2025, 1, 15)
print(tday - bday)
print((tday - bday).days)
print((tday - bday).total_seconds())