

def find_word(num_let, max_ssw):

    WORD_LIST = ["question", "security", "southern", "null",
                 "etadidnac", "candidate",
                 "pasport", "support"]

    if num_let == 0 or max_ssw == 0:
        return None

    exactSswWords = []
    highestSsw = ""

    for word in WORD_LIST:
        if len(word) != num_let:
            continue

        ssw = 0
        for letter in word:
            ssw = ssw + ord(letter)

        if ssw == max_ssw:
            exactSswWords.append((ssw, word))
        elif not exactSswWords and ssw < max_ssw:
            highestSsw = word
        else:
            # ssw > max_ssw
            pass

    if exactSswWords:
        return exactSswWords.pop()[-1]
    elif highestSsw:
        return highestSsw
    else:
        return None


if __name__ == "__main__":

    assert find_word(0, 888) is None

    assert find_word(888, 0) is None

    num_let = 8
    max_ssw = 888
    assert find_word(num_let, max_ssw) == 'southern', "test southern"

    num_let = 9
    max_ssw = 500
    assert find_word(num_let, max_ssw) is None, "test None"

    num_let = 9
    max_ssw = 925
    assert find_word(num_let, max_ssw) == "candidate"

    num_let = 7
    max_ssw = 1412
    assert find_word(num_let, max_ssw) == "support"
