from time import sleep

def countDown(number):
    for i in range(number, 0, -1):
        import pdb
        # set break point
        pdb.set_trace()
        print(i)
        sleep(1)


if __name__=="__main__":
    seconds = 10
    countDown(seconds)