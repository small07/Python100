#The difference is that raw_input() does not exist in Python 3.x,
# while input() does. Actually, the old raw_input() has been renamed to input(), and the old input() is gone,
# but can easily be simulated by using eval(input()). (Remember that eval() is evil.
# try to use safer ways of parsing your input if possible.)

y = int(raw_input('input a year here!::'))

def isLeapYear(y):
    return (y%400==0 or (y%4==0 and y%100!=0))

if(isLeapYear(y)):
    print 'This is a leap year!'
else:
    print 'This is not a leap year!'







