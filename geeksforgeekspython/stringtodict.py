words_str=input("enter the words with spaces:")
words={word:len(word) for word in words_str.split()}
print(words)
