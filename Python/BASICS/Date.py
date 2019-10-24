##Import current date module

import datetime as dt

##current datetime 
x=dt.datetime.now()
print(x)

##current date
y=dt.date.today()
print(y)


##change date
y=dt.date(2019,5,25)
print(y)

##import ca;lendar 
import calendar

newcal=calendar.month(2019,5)
print(newcal)