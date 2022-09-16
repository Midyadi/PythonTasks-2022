M, lst = int(input()), [int(i) for i in input().split()]
pairs = set()
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        x,y = lst[i],lst[j]
        if x+y==M:
            pairs.add((x,y))
for pair in sorted(pairs):
    print(*sorted(pair))
