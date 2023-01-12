
def facto(x):
    y = 1
    if x == 1 or x == 0:
        return y
    else:
        for i in range(1,x+1):
            y=y*i
    return y

