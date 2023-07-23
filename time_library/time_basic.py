import datetime
from datetime import date
from datetime import time
import time



bugun = date.today()
print(bugun)

gun = date(2020,12,1)
print(gun)

print(bugun-gun)

yarin = bugun + datetime.timedelta(days=1)
print(yarin)

print(date.isocalendar(bugun))  # yılın hangi haftası ve haftanın kaçıncı günü (pazartesi birinci olarak gün)

print(date.weekday(bugun))   # haftanın kaçıncı günü (pazartesi sfır olarak) 

print(date.ctime(bugun)) # detaylı şekilde tarih


zaman = time(21,15,5)
print(zaman.second)

dt = datetime.datetime(2020,10,21,11,5,3)
print(dt.hour)


time.time #saniye cinsindenden tarih