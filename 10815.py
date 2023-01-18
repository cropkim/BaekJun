import sys
N = int(input())-1
A = list(map(int,sys.stdin.readline().split()))
M = int(input())
B = list(map(int,sys.stdin.readline().split()))
C = []
A.sort()
def search(array, top, bottom, c):
    while bottom<=top:
        middle = (top+bottom)//2
        if c > array[middle]:
            bottom = middle+1
        elif c < array[middle]:
            top = middle-1
        else: return C.append(1)
    return C.append(0)
for i in B:
    search(A,N,0,i)
print(*C)
