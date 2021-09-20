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
    for textName2 in all_files:
        with open("texts2/"+textName1, encoding="utf-8-sig") as file:
            text1 = file.read().lower()
        with open("texts2/"+textName2, encoding="utf-8-sig") as file:
            text2 = file.read().lower()
        text1 = clearText(text1, letters)
        text2 = clearText(text2, letters)
        textLen1 = len(text1)
        textLen2 = len(text2)

        bigramma1 = generate_bigramma(letters)
        bigramma2 = generate_bigramma(letters)

        bigramma1 = bi_letter_frequency(text1, bigramma1)
        bigramma2 = bi_letter_frequency(text2, bigramma2)


        bi_relative_frequency(text1, bigramma1)
        bi_relative_frequency(text2, bigramma2)


        result = count_distance(len(bigramma1), list(bigramma1.values()), list(bigramma2.values()))
        print(result)
    print("-----")
