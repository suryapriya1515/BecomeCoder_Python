def gen_fib(x,y,a=0,b=1):
    if x==0:
        print(a,b,end=' ')
    elif x==1:
        print(b,end=' ')
    for i in range(3,y+1):
        c=a+b
        if c>=x and c<=y:
            print(c,end=' ')
        a=b
        b=c

x,y=map(int,input().split())
gen_fib(x,y)
