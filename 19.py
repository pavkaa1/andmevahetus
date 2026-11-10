with open("algtekst.txt", "r", encoding="utf-8") as fail:
    tekst = fail.read()

suurtekst = tekst.upper()

with open("suured_tahed.txt", "w", encoding="utf-8") as fail:
    fail.write(suurtekst)

print("Tekst on salvestatud suurtähtedega faili!")