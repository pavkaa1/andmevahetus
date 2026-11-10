
# Loeme õpilaste andmed failist
opilased = []

with open("opilased.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.strip().split(";")

        nimi = osad[0]
        hinded = [int(x) for x in osad[1:]]

        # Arvutame õpilase keskmise hinde
        keskmine = sum(hinded) / len(hinded)

        opilased.append((nimi, keskmine))


# Arvutame kogu klassi keskmise
klassi_keskmine = sum(
    keskmine for nimi, keskmine in opilased
) / len(opilased)


# Salvestame tulemused faili
with open("opilased_aruanne.txt", "w", encoding="utf-8") as fail:

    fail.write("ÕPILASTE TULEMUSTE ARUANNE\n")
    fail.write("------------------------------\n")

    for nimi, keskmine in opilased:
        fail.write(f"{nimi}: keskmine hinne {keskmine:.2f}\n")

    fail.write("------------------------------\n")
    fail.write(f"Klassi keskmine: {klassi_keskmine:.2f}\n")


print("Aruanne salvestati faili opilased_aruanne.txt!")
