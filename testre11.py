

import re
regexp=re.compile(r"\d+")

with open("data.txt") as fic:
    for line in fic:
        if regexp.search(line):
            print(line)