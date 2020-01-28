str1 = raw_input('Please enter a string:')

alp=0
num=0
spa=0
oth=0

for i in range(len(str1)):
    if str1[i].isspace():
        spa +=1
    elif str1[i].isdigit():
        num+=1
    elif str1[i].isalpha():
        alp+=1
    else:
        oth+=1

print('space: ',spa)
print('digit: ',num)
print('alpha: ',alp)
print('other: ',oth)
