a,b=map(int,input().split())
sum=0
while True:
    if a%2:
        sum+=b
    a=a//2
    b=b*2
    if a==0:
        break
print(sum)
