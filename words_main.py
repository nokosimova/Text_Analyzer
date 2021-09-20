import os
import copy
from wordFuncions import *

with open("alphabets/rus" + ".txt", encoding="utf-8-sig") as file:
    lettersAndFrequency = [[char, 0] for char in file.readline().replace("\n", "")]
    letters = [l[0] for l in lettersAndFrequency]
letters.append(' ')
all_files = list(os.listdir("texts2/"))
all_files = sorted(all_files)
for textName1 in all_files:
    print(textName1)
    with open("texts2/"+textName1, encoding="utf-8-sig") as file:
        text = file.read().lower()
        result = words_count(text, letters)
       # print(result)
    print("-----")
