
from unigramFunctions import *
import copy
from bigramFunctions import *
from distanceFunctions import *

with open("alphabets/rus" + ".txt", encoding="utf-8-sig") as file:
    lettersAndFrequency = [[char, 0] for char in file.readline().replace("\n", "")]
    lettersAndFrequency2 = copy.copy(lettersAndFrequency)
    letters = [l[0] for l in lettersAndFrequency]

with open("rus1.txt", encoding="utf-8-sig") as file:
    text1 = file.read().lower()
with open("rus2.txt", encoding="utf-8-sig") as file:
    text2 = file.read().lower()
# for unigrams
text1 = clearText(text1, letters)
textLen1 = len(text1)

text2 = clearText(text2, letters)
textLen2 = len(text1)
lettersAndFrequency =  letter_relative_frequency(text1, dict(lettersAndFrequency))
lettersAndFrequency2 = letter_relative_frequency(text2, dict(lettersAndFrequency2))
count_distance(len(letters), list(lettersAndFrequency.values()), list(lettersAndFrequency2.values()))

# for i in lettersAndFrequency.values():
#    print(i)
#    sum1 += i
# print(sum1)





# for bigrams
text1 = clearText(text1, letters)
textLen1 = len(text1)

text2 = clearText(text2, letters)
textLen2 = len(text1)

#bigramma1 = letter_relative_frequency(letters)
#bigramma2 = letter_relative_frequency(letters)
#bi_relative_frequency(text1, bigramma1)
#bi_relative_frequency(text2, bigramma2)
#count_distance(len(bigramma1), bigramma1.values(), bigramma2.values())


