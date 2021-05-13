n,a,b=map(int,input().split())
dc=0
rdc=0
d=0
x=1
if b>10:
    b=b%10+1
if b==10:
    b=1
while n:
    r=n%10
    n=n//10
    dc+=1
    while dc!=rdc:
        d=d+r*x
        x=x*10
        rdc+=1
while d:
    m=d//(10**(rdc-1))
    d=d%(10**(rdc-1))
    rdc-=1
    if m%a==0:
        m=b
        b+=1
        if b==10:
             b=1
    print(m,end='')
