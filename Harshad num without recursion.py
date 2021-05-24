def isharshad(num):
    temp=num
    res=0
    while(temp):
        r=temp%10
        temp=temp//10
        res=res+r
    return num%res==0

num=int(input())
print(isharshad(num))
