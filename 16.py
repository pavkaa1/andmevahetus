with open("ostunimekiri.txt", "w", encoding="utf-8") as fail:
    while True:
        toode = input("Sisesta toode: ")

        if toode == "STOP":
            break

        fail.write(toode + "\n")

print("Ostunimekiri salvestatud.")