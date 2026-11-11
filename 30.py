andmed = """Mari 5 4 5 3
Jüri 3 4
Anna 5 5 4 5 5
Peeter 2 3 3
Kati 4 5 5 4 5 5
Martin 3 4 4"""

keskmised = []

with open("opilased_aruanne.txt", "w", encoding="utf-8") as fail:

    for rida in andmed.split("\n"):
        osad = rida.split()

        nimi = osad[0]
        hinded = []

        for hinne in osad[1:]:
            hinded.append(int(hinne))

        keskmine = sum(hinded) / len(hinded)

        keskmised.append(keskmine)

        fail.write(nimi + " " + str(round(keskmine, 2)) + "\n")

    klassi_keskmine = sum(keskmised) / len(keskmised)

    fail.write("\nKlassi keskmine: " +
               str(round(klassi_keskmine, 2)))

print("Aruanne on salvestatud faili opilased_aruanne.txt")
print("Klassi keskmine:", round(klassi_keskmine, 2))
