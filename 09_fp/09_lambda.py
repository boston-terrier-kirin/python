days = ["Mon", "tue", "wed"]


def change_words(words, fn):
    for word in words:
        print(fn(word))


# (day) => day.capitalize() ăšćă
change_words(days, lambda day: day.capitalize())
