
import os

FAILINIMI = "hinded.txt"


# Loeme õpilased failist
def loe_andmed():
    opilased = []

    if os.path.exists(FAILINIMI):
        with open(FAILINIMI, "r", encoding="utf-8") as fail:
            for rida in fail:
                osad = rida.strip().split(";")

                if len(osad) == 2:
                    nimi = osad[0]
                    hinne = int(osad[1])
                    opilased.append((nimi, hinne))

    return opilased


# Salvestame õpilased faili
def salvesta_andmed(opilased):
    with open(FAILINIMI, "w", encoding="utf-8") as fail:
        for nimi, hinne in opilased:
            fail.write(f"{nimi};{hinne}\n")


# 1. Kuvame kõik õpilased
def kuva_opilased(opilased):
    if not opilased:
        print("Õpilasi veel ei ole.")
    else:
        print("\nÕPILASTE NIMEKIRI")
        print("------------------")

        for nimi, hinne in opilased:
            print(f"{nimi}: hinne {hinne}")


# 2. Lisame uue õpilase
def lisa_opilane(opilased):
    nimi = input("Sisesta õpilase nimi: ").strip()

    try:
        hinne = int(input("Sisesta hinne (1-5): "))

        if not nimi:
            print("Nimi ei tohi olla tühi.")
        elif hinne < 1 or hinne > 5:
            print("Hinne peab olema vahemikus 1-5.")
        else:
            opilased.append((nimi, hinne))
            salvesta_andmed(opilased)
            print("Õpilane lisati edukalt!")

    except ValueError:
        print("Palun sisesta korrektne täisarv!")


# 3. Otsime õpilast
def otsi_opilast(opilased):
    nimi = input("Sisesta otsitava õpilase nimi: ").strip()

    leitud = False

    for opilane, hinne in opilased:
        if opilane.lower() == nimi.lower():
            print(f"Õpilane: {opilane}, hinne: {hinne}")
            leitud = True

    if not leitud:
        print("Õpilast ei leitud.")


# 4. Kuvame hinnete statistika
def statistika(opilased):
    if not opilased:
        print("Statistika kuvamiseks pole andmeid.")
        return

    hinded = [hinne for nimi, hinne in opilased]

    keskmine = sum(hinded) / len(hinded)

    print("\nHINNETE STATISTIKA")
    print("------------------")
    print(f"Hinnete keskmine: {keskmine:.2f}")

    for hinne in range(1, 6):
        arv = hinded.count(hinne)
        print(f"Hinne {hinne}: {arv} korda")


# 5. Salvestame aruande faili
def salvesta_aruanne(opilased):
    aruanne = []

    aruanne.append("ÕPILASTE HINNETE ARUANNE")
    aruanne.append("------------------------------")

    for nimi, hinne in opilased:
        aruanne.append(f"{nimi}: hinne {hinne}")

    aruanne.append("")

    if opilased:
        hinded = [hinne for nimi, hinne in opilased]
        keskmine = sum(hinded) / len(hinded)

        aruanne.append(f"Hinnete keskmine: {keskmine:.2f}")
        aruanne.append("")
        aruanne.append("HINNETE ESINEMISSAGEDUS")

        for hinne in range(1, 6):
            arv = hinded.count(hinne)
            aruanne.append(f"Hinne {hinne}: {arv} korda")
    else:
        aruanne.append("Õpilasi veel ei ole.")

    with open("aruanne.txt", "w", encoding="utf-8") as fail:
        for rida in aruanne:
            fail.write(rida + "\n")

    print("Aruanne salvestati faili aruanne.txt!")


# PÕHIPROGRAMM
opilased = loe_andmed()

while True:
    print("\n===== ÕPILASTE HINNETE HALDAMINE =====")
    print("1. Kuva kõik õpilased")
    print("2. Lisa uus õpilane ja hinne")
    print("3. Otsi õpilast")
    print("4. Kuva hinnete statistika")
    print("5. Salvesta aruanne faili")
    print("6. Lõpeta")

    valik = input("Tee oma valik (1-6): ")

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
        print("Programm lõpetati. Head aega!")
        break

    else:
        print("Vale valik! Palun vali 1-6.")
