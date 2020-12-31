import re

pattern = r'\b_(?P<name>[a-zA-Z0-9]+)\b'
text = input()

matches = re.findall(pattern, text)

print(','.join(matches))

# pattern = r'\b_[a-zA-Z0-9]+\b'
# text = input()
#
# matches = [x[1:] for x in re.findall(pattern, text)]
#
# print(','.join(matches))


