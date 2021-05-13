num,sv,rv=map(int,input().split())
nn=0
temp=num
c=0
if rv==10:
    rv=1
elif rv>10:
    rv=rv%10+1
while num:
    r=num%10
    num=num//10
    c+=1
num=temp
c=c-1
while c!=-1 or num!=0:
    r=num//pow(10,c)
    num=num%pow(10,c)
    c-=1
    if r%sv==0:
        r=rv
        rv+=1
        if rv==10:
            rv=1
    nn=nn*10+r
print(nn)
