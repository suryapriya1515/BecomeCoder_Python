def isfib(n):
    if n==0 or n==1:
        return True
    a=0
    b=1
    while True:
        c=a+b
        if c==n:
            return True
        if c>n:
            return False
        a=b
        b=c

t=int(input())
for _ in range(t):
    n=int(input())
    print(isfib(n))
