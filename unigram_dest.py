import os
import copy
from unigramFunctions import *
from bigramFunctions import *
from distanceFunctions import *

with open("alphabets/rus" + ".txt", encoding="utf-8-sig") as file:
    lettersAndFrequency = [[char, 0] for char in file.readline().replace("\n", "")]
    letters = [l[0] for l in lettersAndFrequency]

all_files = list(os.listdir("texts2/"))
all_files = sorted(all_files)
for textName1 in all_files:
    print(textName1)
    res = []
    for textName2 in all_files:
        with open("texts2/"+textName1, encoding="utf-8-sig") as file:
            text1 = file.read().lower()
        with open("texts2/"+textName2, encoding="utf-8-sig") as file:
            text2 = file.read().lower()
        text1 = clearText(text1, letters)
        text2 = clearText(text2, letters)

        lettersDict1 = copy.copy(lettersAndFrequency)
        lettersDict2 = copy.copy(lettersAndFrequency)

        lettersDict1 = letter_relative_frequency(text1, dict(lettersDict1))
        lettersDict2 = letter_relative_frequency(text2, dict(lettersDict2))
        result = count_distance(len(letters), list(lettersDict1.values()), list(lettersDict2.values()))
        print(result)
    print("-----")
