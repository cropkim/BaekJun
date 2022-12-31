li = [int(input()) for _ in range(2)]

for i in range (li[1]):
    a, b = map(int,input().split())
    li[0] = li[0]-(a*b)
    
if li[0] == 0:
    print("Yes")
else:print("No")    