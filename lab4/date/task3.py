from datetime import datetime,timedelta
import datetime
x=datetime.datetime.now()
microsec=int(x.strftime("%f"))
a=timedelta(microseconds=microsec)
res=x-a
print(res)
