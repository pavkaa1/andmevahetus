fail = open("arvud.txt", "r")
arvud = []

for rida in fail:
    arvud.append(int(rida))

fail.close()

suurim = max(arvud)
vaikseim = min(arvud)

print("Suurim arv:", suurim)
print("Väikseim arv:", vaikseim)
print("Vahe:", suurim - vaikseim)