n = int(input())
matrix = [[0] * n for _ in range(n)]
for line in range(n):
    for column in range(n):
        matrix[line][column] = max(line, column)
for Line in matrix:
    print(*Line)
