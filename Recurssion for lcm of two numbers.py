def Lcm(a,b,t):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*Lcm(a//t,b//t,t)
    else:
        return Lcm(a,b,t+1)
a,b=map(int,input().split())
print(Lcm(a,b,2))
