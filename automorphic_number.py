#This program checks if a given number is an automorphic number or not. 
n=input("Enter a number to check if it is an automorphic number: ")
digits=len(n)
n=int(n)
sq=int(n**2)
print("The square of",n,"is",sq)
if sq%(10**digits)==n:
    print(n,"is an automorphic number")
else:
    print(n,"is not an automorphic number")