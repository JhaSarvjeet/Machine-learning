# Write a program that asks the user to input numbers until they input 0. 
# The program should print the sum of all the input numbers.
sumOfInput=0
while(True):
    num=int(input("enter number"))
    if(num==0):
        break
    sumOfInput+=num
print(f"sum of number is {sumOfInput}")

