"""
Bubble Sort

Description:
Sorts a list of integers in ascending order using Bubble Sort.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

l = int(input("Enter the number of elements: "))
arr=[]
for i in range(0,l):
    arr.append(int(input(f"Enter element {i+1}: ")))
for i in range(0,l-1):
    for j in range(0,l-1-i):
        if(arr[j]>arr[j+1]):
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
print("\nSorted Array: ",arr)