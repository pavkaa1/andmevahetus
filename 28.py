temperatuurid = []

with open("temperatuurid.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.split()
        paev = osad[0]
        temperatuur = int(osad[1])
        temperatuurid.append((paev, temperatuur))

keskmine = sum(temp for paev, temp in temperatuurid) / len(temperatuurid)

soojem = max(temperatuurid, key=lambda x: x[1])
kulmem = min(temperatuurid, key=lambda x: x[1])

ule_15 = sum(1 for paev, temp in temperatuurid if temp > 15)

with open("temperatuuri_aruanne.txt", "w", encoding="utf-8") as fail:
    fail.write("Temperatuuride analüüs\n")
    fail.write("----------------------\n")
    fail.write(f"Nädala keskmine temperatuur: {keskmine:.2f} kraadi\n")
    fail.write(f"Kõige soojem päev: {soojem[0]} ({soojem[1]} kraadi)\n")
    fail.write(f"Kõige külmem päev: {kulmem[0]} ({kulmem[1]} kraadi)\n")
    fail.write(f"Päevi üle 15 kraadi: {ule_15}\n")

print("Temperatuuride analüüs on salvestatud faili temperatuuri_aruanne.txt")
