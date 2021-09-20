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

# for bigrams
text1 = clearText(text1, letters)
textLen1 = len(text1)

text2 = clearText(text2, letters)
textLen2 = len(text2)

bigramma1 = generate_bigramma(letters)
bigramma2 = generate_bigramma(letters)

bigramma1 = bi_letter_frequency(text1, bigramma1)
bigramma2 = bi_letter_frequency(text2, bigramma2)

sum1 = sum(list(bigramma1.values()))
sum2 = sum(list(bigramma2.values()))
print("суммы")
print((textLen1, "   ", sum1))
print((textLen2, "   ", sum2))

bi_relative_frequency(text1, bigramma1)
bi_relative_frequency(text2, bigramma2)
count_distance(len(bigramma1), list(bigramma1.values()), list(bigramma2.values()))


