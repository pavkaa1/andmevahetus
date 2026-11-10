def raha_eurodes(umber, hind):
    return umber * 5 * hind / 100

fail = input("Faili nimi: ")
hind = int(input("Kilo hind sentides: "))

f = open(fail)
kokku = 0
paev = 1

for rida in f:
    raha = raha_eurodes(int(rida), hind)
    print(paev, ". päeval sai", raha, "eurot")
    kokku = kokku + raha
    paev = paev + 1

f.close()

print("Kokku sai:", kokku)