
import os
import re
from collections import Counter

# Küsime kasutajalt failinime
failinimi = input("Sisesta analüüsitava tekstifaili nimi: ")

# Kontrollime, kas fail on olemas
if not os.path.exists(failinimi):
    print("Viga! Sellist faili ei leitud.")

else:
    # Loeme faili sisu
    with open(failinimi, "r", encoding="utf-8") as fail:
        tekst = fail.read()

    # Leiame sõnad
    sonad = re.findall(r"\b\w+\b", tekst.lower())

    # Sõnade arv
    sonade_arv = len(sonad)

    # Lausete arv
    laused = re.findall(r"[.!?]+", tekst)
    lausete_arv = len(laused)

    # Pikim sõna
    if sonad:
        pikim_sona = max(sonad, key=len)
    else:
        pikim_sona = "Puudub"

    # Viis kõige sagedamini esinevat sõna
    sagedus = Counter(sonad)
    sagedasemad = sagedus.most_common(5)

    # Koostame aruande
    aruanne = []

    aruanne.append("TEKSTIANALÜÜSI ARUANNE")
    aruanne.append("------------------------------")
    aruanne.append(f"Analüüsitud fail: {failinimi}")
    aruanne.append(f"Sõnade arv: {sonade_arv}")
    aruanne.append(f"Lausete arv: {lausete_arv}")
    aruanne.append(f"Pikim sõna: {pikim_sona}")
    aruanne.append("")
    aruanne.append("5 kõige sagedamini esinevat sõna:")

    for sona, arv in sagedasemad:
        aruanne.append(f"{sona}: {arv} korda")

    # Kuvame tulemused ekraanil
    for rida in aruanne:
        print(rida)

    # Salvestame tulemused faili
    with open("tekstianaluus.txt", "w", encoding="utf-8") as fail:
        for rida in aruanne:
            fail.write(rida + "\n")

    print("\nTulemused salvestati faili tekstianaluus.txt")
