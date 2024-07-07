#Write a program that prints the first n Fibonacci numbers, where n is input by the user.
num=int(input("enter number"))
if(num==1):
    print(0)
elif num==2:
    print(0, ' ',1 )
else:
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(1,num-1):
        c=a+b
        print(c,end=" ")
        a,b=b,c


