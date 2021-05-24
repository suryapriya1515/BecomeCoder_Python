def Lcm(a,b):
    t=2
    res=1
    while a>=0 and b>=t:
        if a%t==0 and b%t==0:
            a=a//t
            b=b//t
            res=res*t
        else:
            t+=1
    return res*a*b
a,b=map(int,input().split())
print(Lcm(a,b))
