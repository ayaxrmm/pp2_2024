import re
txt="abbbb"
x=re.findall("a[b]{2,3}", txt)
print(x)

