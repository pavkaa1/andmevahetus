paaris = 0
paaritu = 0

with open("arvud.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        arv = int(rida.strip())

        if arv % 2 == 0:
            paaris += 1
        else:
            paaritu += 1

print(f"Paarisarve: {paaris}")
print(f"Paarituid arve: {paaritu}")