# Binary Search Program
# This program accepts a list of integers from the user,
# sorts the list, and searches for a given element using
# the Binary Search algorithm.

ln=int(input("Enter the length of the list: "))

#Create an empty list to store the numbers
list=[]       
check=False

#input the numbers from the user and append them to the list
for i in range(ln):                      
    num=int(input("Enter the number:"))
    list.append(num)
list.sort()
n=int(input("Enter the number to search:"))
mn=0
mx=ln-1
while mn<=mx:
    mid=int((mn+mx)/2)
    if(list[mid]==n):
        print("the number is found at index",mid)
        check=True
        break
    elif(list[mid]<n):
        mn=mid+1
    elif(list[mid]>n):
        mx=mid-1
if(check==False):
    print("the number is not found")