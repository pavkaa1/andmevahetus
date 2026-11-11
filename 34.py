
import os

algandmed = {
    "Mari": [5, 4, 5, 3],
    "Jüri": [3, 4],
    "Anna": [5, 5, 4, 5, 5],
    "Peeter": [2, 3, 3],
    "Kati": [4, 5, 5, 4, 5, 5],
    "Martin": [3, 4, 4]
}

if not os.path.exists("hinded.txt"):
    with open("hinded.txt", "w", encoding="utf-8") as fail:
        for nimi, hinded in algandmed.items():
            fail.write(nimi + " " +
                       " ".join(map(str, hinded)) + "\n")


def loe_andmed():
    opilased = {}

    with open("hinded.txt", "r", encoding="utf-8") as fail:
        for rida in fail:
            osad = rida.split()
            if len(osad) > 1:
                nimi = osad[0]
                hinded = [int(x) for x in osad[1:]]
                opilased[nimi] = hinded

    return opilased


def salvesta_andmed(opilased):
    with open("hinded.txt", "w", encoding="utf-8") as fail:
        for nimi, hinded in opilased.items():
            fail.write(nimi + " " +
                       " ".join(map(str, hinded)) + "\n")


def kuva_opilased(opilased):
    for nimi, hinded in opilased.items():
        print(nimi, "Hinded:", hinded)


def lisa_opilane(opilased):
    nimi = input("Sisesta õpilase nimi: ")

    try:
        hinne = int(input("Sisesta hinne (1-5): "))

        if hinne < 1 or hinne > 5:
            print("Hinne peab olema 1 kuni 5!")
            return

        if nimi in opilased:
            opilased[nimi].append(hinne)
        else:
            opilased[nimi] = [hinne]

        salvesta_andmed(opilased)
        print("Hinne lisatud!")

    except ValueError:
        print("Palun sisesta õige hinne!")


def otsi_opilast(opilased):
    nimi = input("Keda otsid? ")

    if nimi in opilased:
        print(nimi, "Hinded:", opilased[nimi])
    else:
        print("Õpilast ei leitud!")


def statistika(opilased):
    koik_hinded = []

    for hinded in opilased.values():
        koik_hinded.extend(hinded)

    if len(koik_hinded) == 0:
        print("Hindeid pole!")
        return

    keskmine = sum(koik_hinded) / len(koik_hinded)

    print("Hinnete keskmine:", round(keskmine, 2))
    print("Hinnete esinemissagedus:")

    for hinne in range(1, 6):
        arv = koik_hinded.count(hinne)
        print(hinne, ":", arv, "korda")


def salvesta_aruanne(opilased):
    with open("aruanne.txt", "w", encoding="utf-8") as fail:
        for nimi, hinded in opilased.items():
            keskmine = sum(hinded) / len(hinded)
            fail.write(nimi + " - " +
                       str(round(keskmine, 2)) + "\n")

        koik_hinded = []

        for hinded in opilased.values():
            koik_hinded.extend(hinded)

        if koik_hinded:
            keskmine = sum(koik_hinded) / len(koik_hinded)
            fail.write("\nKlassi keskmine: " +
                       str(round(keskmine, 2)))

    print("Aruanne salvestatud faili aruanne.txt!")


opilased = loe_andmed()

while True:
    print("\n--- ÕPILASTE HINNETE HALDAMINE ---")
    print("1. Kuva kõik õpilased")
    print("2. Lisa uus õpilane ja hinne")
    print("3. Otsi õpilast")
    print("4. Kuva hinnete statistika")
    print("5. Salvesta aruanne faili")
    print("6. Lõpeta")

    valik = input("Tee valik: ")

    if valik == "1":
        kuva_opilased(opilased)

    elif valik == "2":
        lisa_opilane(opilased)

    elif valik == "3":
        otsi_opilast(opilased)

    elif valik == "4":
        statistika(opilased)

    elif valik == "5":
        salvesta_aruanne(opilased)

    elif valik == "6":
        salvesta_andmed(opilased)
        print("Programm lõpetatud!")
        break

    else:
        print("Vale valik! Proovi uuesti.")
