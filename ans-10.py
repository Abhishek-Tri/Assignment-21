#Write a recursive python function to print a number in reverse order

def printRev(n):
    if n>0:
        print(n%10,end='')      #number in reverse
        printRev(n//10)

num=int(input("Enter a number :"))   
printRev(num)   
