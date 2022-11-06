# https://pypi.org/project/translate/
from translate import Translator

try:
    with open("./test/en.txt", mode="r") as my_file:
        text = my_file.read()
        translator = Translator(to_lang="ja")
        translation = translator.translate(text)

        with open("./test/ja.txt", mode="w", encoding="utf-8") as my_ja_file:
            my_ja_file.write(translation)

except FileNotFoundError as e:
    print(e)
