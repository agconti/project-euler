import string


def test_score():
    names = ["MARY", "PATRICIA", "LINDA"]
    assert score(names) == 385


def names_scores_sequence(names, letter_score_key):
    for position, name in enumerate(names):
        yield (position + 1) * score_letters(name, letter_score_key)


def score_letters(name, letter_score_key):
    return sum(letter_score_key[letter] for letter in name)


def score(names):
    names.sort()
    letter_score_key = {letter: score + 1 for score, letter in enumerate(string.letters)}
    return sum(names_scores_sequence(names, letter_score_key))
