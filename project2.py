#This program performs word counting operation.
#This program gives the word count of the given input text.

print("---WELCOME TO WORD COUNTING---")

def count_words(text):
    words = text.split()
    return len(words)

data = input("Enter the text: ")
if data.strip():
    print("Entered data: ", data)
    word_count = count_words(data)
    print("Words: ", data.split())
    print("Word count of the entered text is: ", word_count)
else:
    print("No text entered. Please enter some text.")
