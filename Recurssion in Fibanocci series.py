def fibi(a,b,d,num):
    if d>num:
        return
    if d==1:
        print(a,end=' ')
        d+=1
    if d==2:
        print(b,end=' ')
        d+=1
    print(a+b,end=' ')
    fibi(b,a+b,d+1,num)
num=int(input())
fibi(0,1,1,num)
