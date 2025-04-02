# Program to count the number of words in a given string

def count_words(sentence):
    words = sentence.split()
    return len(words)

# Modify the program to count word frequency
def count_words_and_frequency(sentence):
    words = sentence.split()
    word_count = len(words)
    word_frequency = {}
    
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    return word_count, word_frequency

# Get user input
sentence = input("Enter a sentence: ")

# Get word count and frequency
word_count, word_frequency = count_words_and_frequency(sentence)
print(f"Total word count: {word_count}")
print("Word frequency:", word_frequency)
