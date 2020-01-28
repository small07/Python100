

a = raw_input('add number:')
b = int(raw_input('How many times?'))

res = 0

for i in range(1,b):
    res += int(a)
    a += a[0]
print ('the result is:',res+int(a))

##need further review