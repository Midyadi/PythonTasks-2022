n,m = int(input()), int(input())
a = [[0]*m for i in range(n)]
for q in range(n):
    for w in range(m):
        if q>w:
            a[q][w]=2
        elif w>q:
            a[q][w] = 1
        else:
            a[q][w] = 0
for p in a:
    print(*p)