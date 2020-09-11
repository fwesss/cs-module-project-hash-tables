from itertools import product

"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


if __name__ == "__main__":
    calculations = {}

    combos = product(q, repeat=4)
    answers = []

    for combo in combos:
        a, b, c, d = None, None, None, None

        if combo[0] in calculations:
            a = (combo[0], calculations[combo[0]])
        else:
            a = (combo[0], f(combo[0]))
            calculations[combo[0]] = f(combo[0])

        if combo[1] in calculations:
            b = (combo[1], calculations[combo[1]])
        else:
            b = (combo[1], f(combo[1]))
            calculations[combo[1]] = f(combo[1])

        if combo[2] in calculations:
            c = (combo[2], calculations[combo[2]])
        else:
            c = (combo[2], f(combo[2]))
            calculations[combo[2]] = f(combo[2])

        if combo[3] in calculations:
            d = (combo[3], calculations[combo[3]])
        else:
            d = (combo[3], f(combo[3]))
            calculations[combo[3]] = f(combo[3])

        if a[1] + b[1] == c[1] - d[1]:
            answers.append([a, b, c, d])

    for answer in answers:
        print(
            f"f({answer[0][0]}) + f({answer[1][0]}) = f({answer[2][0]}) - f({answer[3][0]})  {answer[0][1]} + {answer[1][1]} = {answer[2][1]} - {answer[3][1]}"
        )
