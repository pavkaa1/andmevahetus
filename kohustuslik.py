
import os

# Kontrollime, kas fail on olemas
if not os.path.exists("tulemused.txt"):
    print("Viga! Faili tulemused.txt ei leitud.")
else:

    opilased = []

    # Loeme andmed failist
    with open("tulemused.txt", "r", encoding="utf-8") as fail:
        for rida in fail:
            osad = rida.strip().split(";")

            nimi = osad[0]
            tulemused = [int(x) for x in osad[1:]]

            # Arvutame keskmise
            keskmine = sum(tulemused) / len(tulemused)

            # Määrame hinde
            if keskmine >= 90:
                hinne = 5
            elif keskmine >= 75:
                hinne = 4
            elif keskmine >= 60:
                hinne = 3
            elif keskmine >= 50:
                hinne = 2
            else:
                hinne = 1

            opilased.append((nimi, keskmine, hinne))

    # Koostame aruande
    aruanne = []

    aruanne.append("ÕPILASTE TULEMUSTE ARUANNE")
    aruanne.append("------------------------------")
    aruanne.append("")

    # Kuvame iga õpilase tulemused
    for nimi, keskmine, hinne in opilased:
        rida = f"{nimi:<10} Keskmine: {keskmine:.2f}  Hinne: {hinne}"
        aruanne.append(rida)

    aruanne.append("")
    aruanne.append("------------------------------")

    # Leiame klassi keskmise
    klassi_keskmine = sum(
        opilane[1] for opilane in opilased
    ) / len(opilased)

    # Leiame parima ja nõrgima õpilase
    parim = max(opilased, key=lambda x: x[1])
    noorim = min(opilased, key=lambda x: x[1])

    # Loendame positiivse hindega õpilased
    positiivsed = sum(
        1 for opilane in opilased if opilane[2] >= 3
    )

    # Lisame kokkuvõtte
    aruanne.append(f"Klassi keskmine: {klassi_keskmine:.2f}")
    aruanne.append(f"Parim õpilane: {parim[0]}")
    aruanne.append(f"Nõrgim õpilane: {noorim[0]}")
    aruanne.append(f"Positiivse hindega õpilasi: {positiivsed}")

    # Kuvame aruande terminalis
    for rida in aruanne:
        print(rida)

    # Salvestame aruande faili
    with open("aruanne.txt", "w", encoding="utf-8") as fail:
        for rida in aruanne:
            fail.write(rida + "\n")

    print("\nAruanne salvestati faili aruanne.txt")
