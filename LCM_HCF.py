n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
if n1>n2:
    lar=n1
    sm=n2
else:
    lar=n2
    sm=n1
while lar != sm:
    if lar > sm:
        lar = lar - sm
    else:
        sm = sm - lar
hcf=int(lar)
lcm=int((n1*n2)/hcf)
print("HCF of",n1,"and",n2,"is",hcf)
print("LCM of",n1,"and",n2,"is",lcm)
