for x in range(1, 100):
    if((x%3==0) & (x%7==0)):
        print(x)

for x in range(1, 100):
    if((x%7==0)&(x%3==1)):
        print(x)

def isdivisible():
    for x in range(1, 100):
        if x % 2 == 1 and x % 7 == 0 and x % 3 == 1:
            print(x)


isdivisible()

