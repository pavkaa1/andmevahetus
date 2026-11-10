from urllib.request import urlopen

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

with urlopen(url) as response:
    data = response.read()
    text = data.decode("utf-8")

lines = text.splitlines()

for i, line in enumerate(lines[:10], start=1):
    print(f"{i}. {line}")
