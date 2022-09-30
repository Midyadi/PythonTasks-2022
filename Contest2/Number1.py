n, m = int(input()), int(input())
print([[(n+1)*line+column for column in range(m)] for line in range(n)])
