def no_dups(s):
    unique = {}
    for index, word in enumerate(s.split()):
        if word not in unique:
            unique[word] = index

    return " ".join([word for word in unique.keys()])


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
