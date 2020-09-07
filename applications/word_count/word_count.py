def word_count(s):
    def is_valid(character):
        invalid = [
            '"',
            ":",
            ";",
            ",",
            ".",
            "-",
            "+",
            "=",
            "/",
            "\\",
            "|",
            "[",
            "]",
            "{",
            "}",
            "(",
            ")",
            "*",
            "^",
            "&",
        ]

        if character in invalid:
            return False

        return True

    s = "".join(filter(is_valid, s)).lower().split()
    words = set(s)
    word_counts = {word: 0 for word in words}

    for word in words:
        for other_word in s:
            if word == other_word:
                word_counts[word] += 1

    return word_counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )
