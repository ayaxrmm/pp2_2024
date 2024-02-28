import re


txt = "The Rain In Spain"
x = re.split(r"(?=[A-Z])", txt)
print(x)
