
import re

line="nb1 34.5  nb2 67.8  nb3 : 889.99"

reg1=re.compile(r"(\d+\.\d+)")

for result in reg1.finditer(line):
    print(result.group(0))

