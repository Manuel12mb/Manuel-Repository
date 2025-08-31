def search_value(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return i, j
    return None

matrix = [
    [5, 1, 9],
    [1, 6, 2],
    [8, 4, 5]
]

print("Original matrix:")
for row in matrix:
    print(row)

value = 4
result = search_value(matrix, value)
if result:
    row, col = result
    print(f"The value {value} was found at position ({row}, {col})")
else:
    print(f"The value {value} was not found in the matrix")