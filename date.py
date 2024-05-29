# datetime
import datetime
x=datetime.datetime.now()
print(x)

#dateoutput
print(x.year)
print(x.strftime("%A"))

#creating date objects
y=datetime.datetime(2020,5,7)
print(y)

#strftime()
print(x.strftime("%B"))
print(x.strftime("%a"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%z"))
print(x.strftime("%Z"))

