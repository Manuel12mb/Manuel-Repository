def bubble_sort_row(matrix, row):
    n = len(matrix[row])
    for i in range(n):
        for j in range(0, n-i-1):
            if matrix[row][j] > matrix[row][j+1]:
                matrix[row][j], matrix[row][j+1] = matrix[row][j+1], matrix[row][j]

matrix = [
    [3, 1, 6],
    [8, 2, 9],
    [4, 2, 5]
]

print("Original matrix:")
for row in matrix:
    print(row)

row_to_sort = 2
bubble_sort_row(matrix, row_to_sort)

print(f"\nMatrix with row {row_to_sort} sorted:")
for row in matrix:
    print(row)