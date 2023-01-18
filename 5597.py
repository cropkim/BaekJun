students=list(i for i in range(1,31))
for _ in range(28):
    i = int(input())
    students.remove(i)
print(students[0],students[1],sep="\n")