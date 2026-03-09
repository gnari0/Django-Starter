filePath = 'djangoStarter/main/templates/asciiOriginal.txt'
txt = ''
try:
    with open(filePath, 'r', encoding='utf-8') as file:
        txt = file.read()
        ans = ""
        for line in txt.splitlines():
            half = line[:int(len(line) / 2) + 4]
            print(half)
            ans += half
            ans += half[::-1]
            ans += '\n'
    with open('djangoStarter/main/templates/ascii.txt', 'w', encoding='utf-8') as file:
        file.write(ans)
except Exception as e:
    print(f"error flipping ascii: {e}")