# Function to count the frequency of each word in a text
def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

# Test the function
sample_text = "this is a test this is only a test"
print(f"Word frequency: {word_frequency(sample_text)}")
