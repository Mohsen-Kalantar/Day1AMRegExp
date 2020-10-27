
import re

line="value  234  value:256 value::788  value   45 value   234"

reg1=re.compile(r"[\s:]+")

res=reg1.split(line)

print(res[1::2])

import timeit
def f():
    return list(map(int, res[1::2]))
# numbers=list(map(int, res[1::2]))
def g():
    return [int(e) for e in res[1::2]]
print(timeit.timeit(f, setup="from __main__ import f"))
print(timeit.timeit(g, setup="from __main__ import g"))
# numbers=[int(e) for e in res[1::2]] # A list "comprehension"
# print(numbers)
