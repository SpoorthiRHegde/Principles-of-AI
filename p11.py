# Function to take matrix input from the user
def input_matrix(rows, cols):
    matrix = []
    print("Enter the elements of the matrix row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
        while len(row) != cols:
            print(f"Error: Please enter exactly {cols} elements.")
            row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
        matrix.append(row)
    return matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = input_matrix(rows, cols)

print("The entered matrix is:")
for row in matrix:
    print(row)
