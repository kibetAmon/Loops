for x in range(1, 100):
    if x % 3 == 0 and x % 7 == 0:
        print("Numbers divisible by 7 and 3", x)

for x in range(1, 100):
    if x % 7 == 0 and x % 3 != 0:
        print("Numbers divisible by 7 and not 3", x)


for x in range(1, 100):
    if x % 2 != 0 and x % 7 == 0 and x % 3 != 0:
        print("Odd numbers divisible by 7 and not 3", x)

for x in range(1, 100):
    sum_of_digits = sum(int(digit) for digit in str(x))
    if x % sum_of_digits == 0:
        print("Numbers divisible by sum of its digits", x)

for x in range(1, 100):
    sum_of_digits = sum(int(digit) for digit in str(x))
    if(pow(sum_of_digits, 2)) == x:
        print("Numbers that are equal to the square of the sum of its digits", x)



