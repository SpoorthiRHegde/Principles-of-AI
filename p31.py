import matplotlib.pyplot as plt

# Function to plot a simple line graph
def plot_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Simple Line Graph')
    plt.show()

# Test the function
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plot_graph(x, y)
