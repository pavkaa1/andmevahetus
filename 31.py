
# Loeme kontaktid failist
kontaktid = []

with open("kontaktid.txt", "r", encoding="utf-8") as fail:
    for rida in fail:
        osad = rida.strip().split(";")

        nimi = osad[0]
        email = osad[1]
        telefon = osad[2]

        kontaktid.append((nimi, email, telefon))


# Kontaktide otsimine
while True:
    otsing = input("\nSisesta otsitava kontakti nimi (või 'lõpeta'): ")

    # Kontrollime, kas kasutaja soovib lõpetada
    if otsing.lower() == "lõpeta":
        print("Programm lõpetati. Head aega!")
        break

    leitud = False

    # Otsime kontakti nime järgi
    for nimi, email, telefon in kontaktid:
        if nimi.lower() == otsing.lower():
            print("\nKontakt leitud!")
            print("Nimi:", nimi)
            print("E-post:", email)
            print("Telefon:", telefon)

            leitud = True

    if not leitud:
        print("Kontakti ei leitud.")
