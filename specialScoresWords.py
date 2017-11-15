

def find_word(num_let, max_ssw):

    WORD_LIST = ["question", "security", "southern", "null"]

    if num_let == 0 or max_ssw == 0:
        return None

    exactSswWords = []

    for word in WORD_LIST:
        ssw = 0
        for letter in word:
            ssw = ssw + ord(letter)

        if ssw == max_ssw:
            exactSswWords.append([ssw, word])
        else:
            pass

    # assert exactSswWords[0][1] == "southern", "lista mal formada"
    assert [888, "question"] in exactSswWords
    assert [888, "security"] in exactSswWords
    assert [888, "southern"] in exactSswWords

    return exactSswWords.pop()[-1]


if __name__ == "__main__":

    assert find_word(0, 888) is None

    assert find_word(888, 0) is None

    num_let = 8
    max_ssw = 888
    assert find_word(num_let, max_ssw) == 'southern', "test southern"
