# Function to write and read from a file
def write_and_read_file():
    filename = "example.txt"
    
    # Write to the file
    with open(filename, "w") as file:
        file.write("Hello, this is a test file.\n")
        file.write("Let's write some more text.\n")
    
    # Read from the file
    with open(filename, "r") as file:
        content = file.read()
    
    return content

# Test the function
print("File content:\n" + write_and_read_file())
