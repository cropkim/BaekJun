li = [int(input()) for _ in range(2)]
S=0
for i in range (li[1]):
    a, b = map(int,input().split())
    S = S+ a*b
    
if li[0] == S:
    print("Yes")
else:print("No")    