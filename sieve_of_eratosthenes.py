"""
Sieve of Eratosthenes

Description:
Generates all prime numbers up to a given limit using the
Sieve of Eratosthenes algorithm.

Time Complexity: O(n log log n)
Space Complexity: O(n)
"""

N=int(input("Enter the upper limit: "))
is_prime=[True]*(N+1)
if(N>=0):
    is_prime[0]=False
if(N>=1):
    is_prime[1]=False

for i in range(2,int(N**0.5)+1):
    if is_prime[i]:
        j=i*i
        while(j<=N):
            is_prime[j]=False
            j+=i
num=[]
for i in range(2,N+1):
    if is_prime[i]:
        num.append(i)

print(f"Prime numbers up to {N}:")
for prime in num:
    print(prime, end=" ")