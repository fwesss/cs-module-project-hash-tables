def caesar(file):
    with open(file) as f:
        text = f.read()

        letter_count = {}

        for letter in text:
            if letter.isalpha():
                if letter not in letter_count:
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1

        translation = "ETAOHNRISDLWUGFBMYCPKVQJXZ"

        sorted_text = ""
        for letter, _ in sorted(
            letter_count.items(), key=lambda item: item[1], reverse=True
        ):
            sorted_text += letter

        return text.translate(str.maketrans(sorted_text, translation))


if __name__ == "__main__":
    print(caesar("ciphertext.txt"))
