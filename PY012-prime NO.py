import math

for i in range(100,200):
    for j in range(2,int(round(math.sqrt(i))+1)):
        if i%j==0:
            break
        else:
            print(i)