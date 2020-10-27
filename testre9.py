
import re

text="angela bic"

# regexp=re.compile(r"^([abc])(.+)([abc])$")
# 
# matchobj=regexp.search(text)

matchobj=re.search(r"^([abc])(.+)([abc])$",text)

if matchobj:
    print("The string text 'match'")
    print(matchobj.groups())
else:
    print("The string text does not 'match'")

