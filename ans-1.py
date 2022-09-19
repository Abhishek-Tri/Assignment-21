#Write a recursive python function to print first N natural numbers.

def printN(n):
    if n>0:
        printN(n-1)
        print(n)

num=int(input("Enter a number :"))   
printN(num)     
