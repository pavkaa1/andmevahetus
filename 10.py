with open("tekst.txt", "r", encoding="utf-8") as fail:
    tekst = fail.read()

sonad = tekst.split()
arv = len(sonad)

print("Tekstis on", arv, "sõna.")