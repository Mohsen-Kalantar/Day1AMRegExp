import re

line="nb1 34.5  nb2 67.8  nb3 : 889.99"

reg1=re.compile(r"\d+\.\d+")

result=reg1.findall(line)
if result:
    print("Match")
    print(result)
 
else:
    print("No Match")
