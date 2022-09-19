#Write a recursive python function to print first N multiples of a given number.

num=int(input("Enter a number :"))
temp=num
def printmul(n):
   
    if n>0:
        printmul(n-1)
        print(temp*n)

printmul(num)        