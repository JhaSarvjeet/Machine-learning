#Write a program that checks if a number input by the user is a prime number using a for loop.
num=int(input("enter number"))
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")