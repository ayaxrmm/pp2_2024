from datetime import datetime, timedelta
x=timedelta(days=1)

today= datetime.now().date()
tomorrow=today+x
yesterday=today-x

print(yesterday)
print(today)
print(tomorrow)



