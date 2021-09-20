import re
import numpy as np
from decimal import Decimal
def bi_letter_frequency(text, bi_alphabet):
    keys = bi_alphabet.keys()
    for i in range(len(text)-1):
        if (text[i]+text[i+1]) in keys:
            bi_alphabet[text[i]+text[i+1]] += 1
    return bi_alphabet

def bi_relative_frequency(text, bi_alphabet):
    total_count = 0
    # print("абсолютные частоты")
    # for key in bi_alphabet.keys():
    #     print(bi_alphabet[key])
    # print("------------")

    bi_letter_frequency(text, bi_alphabet)
    for i in bi_alphabet.values():
        total_count += i
    for i in bi_alphabet.keys():
        bi_alphabet[i] = bi_alphabet[i] / total_count
    return bi_alphabet


def generate_bigramma(alphabet):
    bigramma = {}
    for i in alphabet:
        for j in alphabet:
            bigramma[i+j] = 0
    return bigramma
