nimi = input("Sisesta oma nimi: ")
vanus = input("Sisesta oma vanus: ")
email = input("Sisesta oma e-posti aadress: ")

# Andmete salvestamine faili
with open("kasutaja.txt", "w", encoding="utf-8") as fail:
    fail.write(nimi + "\n")
    fail.write(vanus + "\n")
    fail.write(email + "\n")

# Faili uuesti avamine ja sisu kuvamine
with open("kasutaja.txt", "r", encoding="utf-8") as fail:
    sisu = fail.read()

print("\nFaili sisu:")
print(sisu)