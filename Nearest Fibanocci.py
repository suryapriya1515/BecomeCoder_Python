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
            if n-b<=c-n:
                print(b,end=' ')
            if n-b>=c-n:
                print(c,end=' ')
            return False
        a=b
        b=c

n=int(input())
print(isfib(n))
