from urllib.request import urlopen

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

response = urlopen(url)

try:
    data = response.read()
    text = data.decode("utf-8")
    print(text)
finally:
    response.close()
