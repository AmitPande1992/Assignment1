from ast import Str
from tkinter.tix import InputOnly


word = input("Enter the word: ")
Reverse_word = ""
count = len(word)
while count > 0:
    Reverse_word += word[count - 1]
    count = count - 1
print("Reverse word is:", Reverse_word)

