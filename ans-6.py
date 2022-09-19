#Write a recursive python function to print first N even natural numbers in reverse order

def printN(n):
    if n>0:
        print(n)
        printN(n-2)

num=int(input("Enter a number :"))   
printN(num*2)     
