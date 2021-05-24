import math as m

def isperfect(num):
    res=1
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            res+=i+num//i
    return res==num
num=int(input())
print(isperfect(num))
