import  time

for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    time.sleep(1)