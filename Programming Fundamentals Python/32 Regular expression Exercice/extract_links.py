import re
pattern = r'((^|(?<=\s))www.[a-zA-Z0-9\-]+(\.?[a-z]+)+($|(?=\s)))'

correct_links = []

while True:
    line = input()
    if not line:
        break
    matches = re.findall(pattern, line)
    if matches:
        link = matches[0]
        correct_links.append(link[0])
        # print(link)

for x in correct_links:
    print(x)