for i in range(100,1000):
    s = str(i)
    # one = int(s[-1])
    # ten = int(s[-2])
    # hun = int(s[-3])
    hun = int(s[0])
    ten = int(s[1])
    one = int(s[2])
    if i == one**3+ten**3+hun**3:
        print (i)