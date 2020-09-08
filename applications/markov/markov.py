import random

# Read in all the words in one go
def markov():
    with open("input.txt") as f:
        words = f.read()

        combos = {}
        first_words = []
        last_words = []
        punctuation = [".", "!", "?"]

        words = words.split()
        for index, word in enumerate(words):
            if word[0].isupper() or (word[0] == '"' and word[1].isupper()):
                first_words.append(word)

            if word[len(word) - 1] in punctuation or (
                word[len(word) - 2] in punctuation and word[len(word) - 1] == '"'
            ):
                last_words.append(word)

            if word not in combos:
                try:
                    combos[word] = set()
                    combos[word].add(words[index + 1])
                except IndexError:
                    break
            else:
                try:
                    combos[word].add(words[index + 1])
                except IndexError:
                    break

        sentence = random.choice(first_words)
        chosen = random.choice(list(combos[sentence]))

        while chosen not in last_words:
            sentence += " " + chosen
            chosen = random.choice(list(combos[chosen]))

        return sentence + " " + chosen


if __name__ == "__main__":
    for _ in range(5):
        print(markov(), "\n")
