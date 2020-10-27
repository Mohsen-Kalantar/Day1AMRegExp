
import re

line="d1 12/03/2001  d2 24/03/2001  d3 24/12/2011"

reg1=re.compile(r"(\d{2})\/(\d{2})\/(\d{4})")

res=reg1.sub(r"\3:\2:\1",line)

print(res)

