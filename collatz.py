def collatz(x):
    if x%2 == 0:
        return x//2
    else:
        return x*3+1
number = int(input("Enter a number. "))
print(number)
count = 0
while number != 1:
    number = collatz(number)
    print(number)
    count+=1
print(str(count)+" steps to 1.")
