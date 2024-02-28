import re
txt="This_is_a_example_STring for This_task"
x=re.findall("[a-z]+[_][a-z]+", txt)
print(x)
