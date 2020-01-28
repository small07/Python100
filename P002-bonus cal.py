profit = int(input("Please enter a number"))
bonus = 0

threashold =[100000,200000,400000,600000,1000000]
ratio = [0.1,0.75,0.05,0.03,0.015,0.001]

if(profit>=1000000):
    for(i=5,i>=0,i--):
        bonus = (profit -threashold[i])*ratio[i]
    if bonus<0:
        print ("working.....")
    else:
        bonus -=bonus

####################################################




