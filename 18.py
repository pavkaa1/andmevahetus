arvud = []

# Viie täisarvu küsimine
for i in range(5):
    arv = int(input("Sisesta täisarv: "))
    arvud.append(arv)

# Arvude salvestamine faili
with open("sisestatud_arvud.txt", "w", encoding="utf-8") as fail:
    for arv in arvud:
        fail.write(str(arv) + "\n")

# Arvude lugemine failist
with open("sisestatud_arvud.txt", "r", encoding="utf-8") as fail:
    arvud = [int(rida) for rida in fail]

# Summa ja keskmise arvutamine
summa = sum(arvud)
keskmine = summa / len(arvud)

# Tulemuste kuvamine
print("Sisestatud arvud:", ", ".join(map(str, arvud)))
print("Summa:", summa)
print("Keskmine:", keskmine)