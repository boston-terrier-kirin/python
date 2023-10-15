# https://regex101.com/

# At least 8 char long
# contain any sort of letters, numbers, $%#@!
# has to end with a number

import re


regex = r"[A-Za-z0-9$%#@!]{8,}\d"
pattern = re.compile(regex)

test_str = "sue123$!4"
result = pattern.search(test_str)
print(result)
print("**********")

test_str = "sue123$!"
result = pattern.search(test_str)
print(result)
