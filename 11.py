import string

with open("tekst.txt", "r", encoding="utf-8") as fail:
    tekst = fail.read()

sonad = tekst.split()

sonad = [sona.strip(string.punctuation) for sona in sonad]

pikim = max(sonad, key=len)

print("Kõige pikem sõna:", pikim)
print("Sõna pikkus:", len(pikim))