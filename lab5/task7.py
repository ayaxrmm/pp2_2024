import re

txt = "The rain in Spain"
r = re.sub(r"\b[a-z]", "R", txt)
print(r)

