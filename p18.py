#matrix division
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()
print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end=" ")
    print()
result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] / matrix2[i][j]
print("division of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()
