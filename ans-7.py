#Write a recursive python function to print squares of first N natural numbers

def printsqr(n):
    if n>0:
        printsqr(n-1)
        print(n*n)

num=int(input("Enter a number :"))   
printsqr(num)     
