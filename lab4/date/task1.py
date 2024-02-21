import datetime
x=datetime.datetime.now()
day= int(x.strftime("%d"))-5
month = x.strftime("%m")
year = x.strftime("%Y")
print(day, "/", month, "/",year)

