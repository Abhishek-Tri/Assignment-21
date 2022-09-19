#Write a recursive python function to print cubes of first N natural numbers

def printcube(n):
    if n>0:
        printcube(n-1)
        print(n**3)

num=int(input("Enter a number :"))   
printcube(num)     
