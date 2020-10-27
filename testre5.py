
import re

text="123 end"
regexp=re.compile(r"(\d+)")

matchobj=regexp.match(text)
if matchobj:
    print(f"The string '{text}' 'match': {matchobj.groups()}")
else:
    print("The string text does not 'match'")

