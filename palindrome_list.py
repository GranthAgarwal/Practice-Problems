len=int(input("Enter the lenght of the list:"))
list=[]
for i in range (len):
    element=input("Enter the element:")
    list.append(element)
list1=list.copy()
list1.reverse()
if(list==list1):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")




