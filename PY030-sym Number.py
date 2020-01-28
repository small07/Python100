n = raw_input('Input what you want:')

a =0

b=len(n)-1

flag = True

while a<b:
    if n[a]<>n[b]:
        print("NOT")
        flag = False
        break
    a,b = a+1,b-1
if flag:
    print ("YES")

#===================
L = [1,2,3,4,5]
print('.'.join(str(n) for n in L))