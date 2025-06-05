import time
def countup_timer(end_time, start_time=0):
        for x in range(start_time, end_time):
            print(x)
            time.sleep(1)
print("done")

countup_timer(60)#parameter feeding is reversed