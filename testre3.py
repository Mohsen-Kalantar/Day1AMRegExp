
import re

"""
\d     <=> [0-9] a digit
\D     <=> [^0-9] is not a digit
\s     a "white space"
\S     any character except a "white space"

[]     a class of character [abc] or [b-e] or [1-6A-C] or ...
+      1 or more occurrence
{min,max} between [min,max] occurrence
{2,}    2 or more
{3}     3 occurrence
{1,} <=> +
{0,} <=> *
{0,1} <=> ?
.    any character except a new line
\.   the character .
^    at the beginning of the string
$    at the end of the string
"""

text="angela bic"
regexp=re.compile(r"^([abc])(.+)([abc])$")

matchobj=regexp.search(text)
if matchobj:
    print("The string text 'match'")
    print(matchobj.groups())
else:
    print("The string text does not 'match'")

