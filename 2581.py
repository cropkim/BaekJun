M = int(input())
if M==1:
    M=M+1
N = int(input())
A = set(i for i in range(M,N+1))
B= set()

for i in A:
    a = int(i**(1/2))
    for k in range(2,a+1):
        if i%k==0:
            B.add(i)
A = A - B
A=list(A)
A=sorted(A)
if len(A)==0:
    print(-1)

else:print(sum(A),A[0],sep="\n")