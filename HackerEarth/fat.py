# Write your code here
def factorsFinder(num1, num2):
    fact_nums = 0
    print(num1)
    print(num2)
    for i in range(1, min(num1, num2)+1):
        if (num1 % i == 0) and (num2 % i == 0):
            fact_nums += 1
    print(fact_nums)
    return fact_nums


if __name__ == "__main__":
    a, b = input().split()
    facts = 0
    a, b = int(a), int(b)
    facts = factorsFinder(10, 15)
    print(facts)


""""
New way
"""

import math
a,b=map(int,input().split())
g=math.gcd(a,b)
r=int(math.sqrt(g))+1
c=0
for i in range(1,r):
    if g%i==0:
        if g/i==i:
            c+=1
        else:
            c+=2
print(c)