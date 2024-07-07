#Write a program that calculates the sum of the 
# digits of a number input by the user using a while loop.

num=int(input('enter number'))
sum=0
while(num):
    sum=sum+(num%10)
    num=num//10
print("sum of entered number is ",sum)