
import datetime

date = datetime.date(2025,1,4)

print(date)

today = datetime.date.today()

print(today)

time = datetime.time(23,53,50)
print(time)

now= datetime.datetime.now()

now = now.strftime("%H:%M:%S %m -%d- %y")    # accessing clases datetime 
print(now) 
print("noicee")