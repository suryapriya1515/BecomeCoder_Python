num=int(input())
mi=num%10
ma=num%10
mi_count=0
ma_count=0
while num:
    r=num%10
    num=num//10
    if r==mi:
        mi_count+=1
    elif r<mi:
        mi=r
        mi_count=1
    if r==ma:
        ma_count+=1
    elif r>ma:
        ma=r
        ma_count=1
print(mi_count,ma_count)
