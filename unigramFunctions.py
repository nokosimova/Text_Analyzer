import re
def letter_frequency(text, alphabet):
    keys = alphabet.keys()
    for letter in text:
        if letter in keys:
            alphabet[letter] += 1
    return alphabet


def letter_relative_frequency(text, alphabet):
    textLen = len(text)
    alphabet = letter_frequency(text, alphabet)
    # print("абсолютные частоты")
    # for key in alphabet.keys():
    #     print(alphabet[key])
    # print("------------")
    for key in alphabet.keys():
        alphabet[key] = alphabet[key] / textLen
    return alphabet


#text cleaning

def defineExtraSigns(text, alphabet):
    extraSigns = text
    #по циклу ищем все элементы не относящиеся к алфавиту:
    for letter in alphabet:
        extraSigns =extraSigns.replace(letter, "")

    result = set(extraSigns)
    return result

def clearText(text, alphabet):
    extra = defineExtraSigns(text, alphabet)
    # print(extra)
    for sign in extra:
        text = text.replace(sign, "")
    return text