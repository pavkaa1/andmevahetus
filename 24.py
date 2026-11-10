from urllib.request import urlopen

url = "https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore"

with urlopen(url) as response:
    data = response.read()
    text = data.decode("utf-8")

lines = text.splitlines()

ridade_arv = len(lines)
sonade_arv = len(text.split())
tahemarkide_arv = len(text)
tuhjade_ridade_arv = sum(1 for line in lines if line.strip() == "")

print("Veebiteksti statistika")
print("----------------------")
print(f"Ridu: {ridade_arv}")
print(f"Sõnu: {sonade_arv}")
print(f"Tähemärke: {tahemarkide_arv}")
print(f"Tühje ridu: {tuhjade_ridade_arv}")
