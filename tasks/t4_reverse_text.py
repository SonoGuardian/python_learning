#Take a sentence input from the user and print it reversed word by word.
#Input: "I love Python" → Output: "Python love I"

text = input('Enter a sentence: ')
words = text.split(' ')

reversed_words =(words[::-1])
reversed_text = " ".join(reversed_words)

print(reversed_text)
