month = int(raw_input('How many months it is?'))

total = 0

if(month <=3):
    total = 1
elif(month>=4):
    for i in range(3,month):
        total +=(i-2)
print total

