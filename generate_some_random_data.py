import random
import time

def readDataRandom():
    hum=random.randint(20,100)
    temp=random.randint(25,50)
    print(hum,temp)
    return (hum,temp)

# while True:
#     readDataRandom()
#     time.sleep(4)