Input: "Let's solve Fanatics contest"
Output: "s'teL evlos scitanaF tsetnoc"


def reverse_word(word):
    n = len(word)
    if n < 2:
        return word
    else:
        result = list(word)
        i = 0
        while i < (n / 2):
            result[i], result[n - 1 - i] = result[n - 1 - i], result[i]
            i += 1
        return "".join(result)


def reverse_word_instring(s):
    if len(s) <= 1:
        return s
    else:
        word_list = s.split(' ')
        for i in range(len(word_list)):
            word_list[i] = reverse_word(word_list[i])

    return " ".join(word_list)


inp = "Let's       solve Fanatics contest"
print(reverse_word_instring(inp))

