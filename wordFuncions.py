import re
def count_wordlen_frequency(text):
    words = text.split()
    word_lens = [len(w) for w in words]
    words_len_frequency = [0 for l in range(0, max(word_lens)+1)]
    for word in words:
        if len(word) in word_lens:
            words_len_frequency[len(word)] += 1

    #print(words)
    for i in range(1, max(word_lens)+1):
        print(words_len_frequency[i])
def words_count(text, alphabet):
    text = clearText(text, alphabet)
    words = text.split()
    print(len(words))
    return words

def count_sentence_lenFrequency(filename):
    with open(filename, encoding="utf-8-sig") as file:
        contents = file.read()
    # удаляем все переходы на новую строку:
    contents = contents.replace("\n", " ")
    contents = contents.replace("\t", " ")
    contents = contents.replace("\r", " ")
    contents = contents.replace("\r\n", " ")

    # удаляем лишние символы
    contents = contents.replace("[", "")
    contents = contents.replace("]", "")
    contents = contents.replace("”", "")
    contents = contents.replace("'", "")
    contents = contents.replace("\"", "")
    contents = contents.replace("...", "")
    contents = re.sub(r"[,/_—:#%@*;()*<>»«^=]", "", contents)
    contents = re.sub(r"[1234567890–-]", "", contents)
    contents = contents.replace('?', '.')
    contents = contents.replace('!', '.')

    sentences = [s.split() for s in contents.split('.')]
    sentences = [s for s in sentences if s != []]

    sentence_lens = [len(s) for s in sentences]
    sentences_len_frequency = [0 for l in range(0, max(sentence_lens)+1)]
    for sentence in sentences:
        if len(sentence) in sentence_lens:
            sentences_len_frequency[len(sentence)] += 1
    #for i in sentences:
    #    print(len(i), "--", i)
    for i in range(1, max(sentence_lens)+1):
        print(sentences_len_frequency[i])

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