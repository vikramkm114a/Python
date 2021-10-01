import random
def randInt(min=0, max=0):
    if min==0 and max==0:
        num=random.random() * 100
    elif min==0:
        num=random.random() * max
    elif max==0:
        num=random.random() * 100 + min
    else:
        num=random.random() * max + min
    print('min: ', min)
    print('max: ', max)
    return num

print(randInt(min=0, max=10))