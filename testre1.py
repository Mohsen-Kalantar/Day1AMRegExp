
import re

text="value 48888 the end"

"""
\d     a digit

+         1 or more occurrence
{min,max} between [min,max] occurrence
{2,}    2 or more
{3}     3 occurrence
{1,} <=> +
{0,} <=> *
{0,1} <=> ?

"""
regexp=re.compile(r"\d+")

if regexp.search(text):
    print("The string text 'match'")
else:
    print("The string text does not 'match'")

