num=int(input())
L=num%10
temp=num//10
c=0
while num:
    r=num%10
    num=num//10
    c=c+1
temp=temp*10+r
temp=temp%pow(10,c-1)
temp=L*pow(10,c-1)+temp
print(temp)
