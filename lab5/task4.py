import re
txt="THis Is an Example FOr tHis Task"
x=re.findall("[A-Z{1}][a-z]+",txt)
print(x)
