# working with times and datetimes
import datetime as dt
import pytz

# time = dt.time(12, 30,50, 600)
# print(time)
# print(time.hour)
# print(time.min)
# print(time.second)
# print(time.microsecond)

# time = dt.datetime(2024, 12, 3,12,45, 6,6000)
# print(time)
# print(time.date())
# print(time.time())

# #  gives current machines today
# dt_today = dt.datetime.today()

# #  gives datetme with timezone option
# dt_now = dt.datetime.now()

# # gives directly utc time
# dt_utc = dt.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utc)


# time_1 = dt.datetime(2016, 2,12, 12,33,45, tzinfo= pytz.UTC)
# print(time_1)
# time_2 = dt.datetime.now(tz= pytz.UTC)
# print(time_2.hour)

#  Now we can get our own time by using timezone functions, it is suggested to use UTC as standarad time
# my_tz = time_2.astimezone(pytz.timezone('Asia/Kolkata'))
# print(my_tz)

# for tz in pytz.all_timezones:
#     print(tz)

#  The thing is if we have a naive timezone, then we can't able to convert it directly into aware timezone
#  we can do below
# first taking soem naive timezone
ind_time = dt.datetime.now()
print(ind_time)
#  we have to use localize function to convert it into aware timezone
time_ind = pytz.timezone('Asia/Kolkata')
ind_time = time_ind.localize(ind_time)
print(ind_time)

#  we can even format the time accoridng to our need
format_time = ind_time.strftime('%d-%B-%Y')
print(format_time)

#  we can even convert a string datetime to datetime object by using strptime
str_time = '12-June-2025'
dtime = dt.datetime.strptime(str_time, '%d-%B-%Y')
print(dtime)