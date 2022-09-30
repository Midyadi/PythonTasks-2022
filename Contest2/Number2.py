n, m = int(input()), int(input())
matrix = [[0] * m for i in range(n)]
for line in range(n):
    for column in range(m):
        if line > column:
            matrix[line][column] = 2
        elif column > line:
            matrix[line][column] = 1
        else:
            matrix[line][column] = 0
for Line in matrix:
    print(*Line)
