def sort_words(sentence):
    words = sentence.split()
    words.sort(key=str.lower) 
    return words

sentence = input("Enter a sentence: ")

sorted_words = sort_words(sentence)
print("Words in alphabetical order:")
print(" ".join(sorted_words))