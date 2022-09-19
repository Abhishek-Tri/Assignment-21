#Write a recursive python function to print first N even natural numbers.

def printN(n):
    if n>0:
        printN(n-2)
        print(n)

num=int(input("Enter a number :"))   
printN(num*2)     
