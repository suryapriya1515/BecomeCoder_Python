num=int(input())
L=num%10
temp=num//10
c=0
while num:
    r=num%10
    num=num//10
    c=c+1
m=temp%pow(10,c-2)
f=r
print(f,L,m)
rev=0
while m:
    r=m%10
    m=m//10
    rev=rev*10+r
print(rev)
rev=rev*10+L
rev=rev%pow(10,c-1)
rev=f*pow(10,c-1)+rev
print(rev)
