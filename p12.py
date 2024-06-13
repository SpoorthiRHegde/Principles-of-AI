# Function to take matrix input from the user
def input_matrix(name, rows, cols):
    matrix = []
    print(f"Enter the elements for the {name} matrix row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
        while len(row) != cols:
            print(f"Error: Please enter exactly {cols} elements.")
            row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
        matrix.append(row)
    return matrix

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

X = input_matrix("first", rows, cols)
Y = input_matrix("second", rows, cols)
result = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        result[i][j] = X[i][j] + Y[i][j]

print("The resulting matrix after addition is:")
for row in result:
    print(row)
