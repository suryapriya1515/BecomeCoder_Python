num=int(input())
temp=num
mi=num%10
ma=num%10
mi_count=0
ma_count=0
while num:
    r=num%10
    num=num//10
    if r>ma:
        ma=r
    if r<mi:
        mi=r
num=temp
while num:
    r=num%10
    num=num//10
    if r==mi:
        mi_count+=1
    elif r==ma:
        ma_count+=1
print(mi_count,ma_count)
