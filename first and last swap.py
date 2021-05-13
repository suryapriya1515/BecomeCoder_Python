num=int(input())
temp=num
count=0
c=0
nn=0
p=1
while num:
    r=num%10
    num=num//10
    count+=1
c=count
num=temp
if num>0:
    first=num//pow(10,count-1)
    last=num%10
while num:
    r=num%10
    num=num//10
    if count==c:
        r=first
    elif count==1:
        r=last
    count-=1
    nn=nn+p*r
    p=p*10
print(nn)
