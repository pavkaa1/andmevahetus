tooted = []

with open("muuk.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()

        nimi = osad[0]
        hind = float(osad[1])
        kogus = int(osad[2])

        tulu = hind * kogus

        tooted.append((nimi, hind, kogus, tulu))

kogu_tulu = sum(toode[3] for toode in tooted)

suurim = max(tooted, key=lambda x: x[3])

with open("muugiaruanne.txt", "w", encoding="utf-8") as fail:
    fail.write("Müügiaruanne\n")
    fail.write("------------------------------\n")

    for nimi, hind, kogus, tulu in tooted:
        fail.write(f"{nimi}: {hind:.2f} x {kogus} = {tulu:.2f} eurot\n")

    fail.write("------------------------------\n")
    fail.write(f"Kogu müügitulu: {kogu_tulu:.2f} eurot\n")
    fail.write(
        f"Suurima müügituluga toode: {suurim[0]} "
        f"({suurim[3]:.2f} eurot)\n"
    )

print("Müügiaruanne on salvestatud faili muugiaruanne.txt")
