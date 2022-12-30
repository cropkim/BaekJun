a=list(map(int,input().split()))
b=set(a)
result = 0
if len(b)==1:
    b= list(b)
    result = 10000+b[0]*1000
elif len(b)==2:
    b = list(b)
    a.remove(b[0])
    a.remove(b[1])
    result = 1000+a[0]*100
else:
    result = max(a)*100
print(result)