from collections import OrderedDict


def histogram(file):
    with open(file) as f:
        words = f.read()

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
                "?",
                "!",
            ]

            if character in invalid:
                return False

            return True

        words = "".join(filter(is_valid, words)).lower().split()

        word_count = {}

        max_length = 0
        for word in words:
            if len(word) > max_length:
                max_length = len(word)

            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

        sorted_words = {
            word: count
            for word, count in sorted(word_count.items(), key=lambda item: item[0])
        }

        for word, count in sorted(
            sorted_words.items(), key=lambda item: item[1], reverse=True
        ):
            print(f"{word}{' ' * (max_length - len(word) + 2)}{'#' * count}")


if __name__ == "__main__":
    histogram("robin.txt")
