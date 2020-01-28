#The difference is that raw_input() does not exist in Python 3.x,
# while input() does. Actually, the old raw_input() has been renamed to input(), and the old input() is gone,
# but can easily be simulated by using eval(input()). (Remember that eval() is evil.
# try to use safer ways of parsing your input if possible.)



def isLeapYear(y):
    return (y%400==0 or (y%4==0 and y%100!=0))

DofM = [0,31,28,31,30,31,30,31,31,30,31,30]

res = 0

year = int(raw_input('input a year'))
month = int(raw_input('input a month'))
day = int(raw_input('input a day'))

if isLeapYear(year):
    DofM[2]+=1
for i in range(month):
    res+=DofM[i]
print(res+day)








