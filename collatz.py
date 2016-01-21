def collatz(x):
    if x%2 == 0:
        return x//2
    else:
        return x*3+1
number = int(input())
print(number)
while number != 1:
    number = collatz(number)
    print(number)
