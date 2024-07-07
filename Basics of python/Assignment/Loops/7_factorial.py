#Write a program that calculates the factorial of a number input by the user using a while loop.

num=int(input('enter number'))
fact=1

while(num>=1):
    fact*=num
    num=num-1
print("factorial of entered number is ",fact)
