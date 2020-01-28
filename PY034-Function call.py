def hello():
    print ("Hello world")

def helloAgain():
    for i in range(3):
        hello()

if __name__ == '__main__':
    helloAgain()