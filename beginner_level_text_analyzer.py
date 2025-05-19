# Beignner level text analyzer code

text = input("Enter text here: ")
len_text = print("length of text is: ",len(text))
count_words = print("The words in text is:",len(text.split()))
find_word = input("Enter word to find from text: ")
if find_word in text.split():
  print("Word is in text")
else:
  print("Word is not in text")
