import datetime

print(datetime.date.today()) ## I18N standard
print(datetime.date(2333,2,26))
print(datetime.date.today().strftime('%d/%m/%Y'))
day=datetime.date(1111,2,3)
day=day.replace(year=day.year+22)
print(day)
