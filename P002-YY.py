total = 0
for i in range(1,5):
   for j in range(1,5):
      for k in range(1,5):
          if(i!=j)and(j!=k)and(i!=k):
              total=total+1
              print(i,j,k)
              print total


