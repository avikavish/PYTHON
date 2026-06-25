
#WAP  to print the factorial of the given number using for loop


n = int(input("enter the number:"))

factorial = 1
for i in range(1,n+1):
    factorial*=i
print("factorial is =",factorial)


