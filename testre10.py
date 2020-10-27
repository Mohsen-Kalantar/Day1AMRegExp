
import re

text="Angela bic"

regexp=re.compile(r"""
                        ^         # The beginning of the text
                        ([abc])   # a group a 1 character a or b or c
                        (.+)      # .....
                        ([abc])
                        $         # The end of the regexp
                        """, re.VERBOSE|re.IGNORECASE)
 
matchobj=regexp.search(text)

if matchobj:
    print("The string text 'match'")
    print(matchobj.groups())
else:
    print("The string text does not 'match'")

