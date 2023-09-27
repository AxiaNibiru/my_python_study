import re


input_str = "Changed in version 3.7: A format string argument is now positional-only."
print(re.sub(r'[^a-zA-Z0-9]', ' ', input_str).strip().split(r' '))
print(re.findall(r'[a-zA-Z0-9]+', input_str))

print(len(re.findall(r'[^a-zA-Z0-9]+', input_str)))
