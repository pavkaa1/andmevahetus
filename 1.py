fail = open("tervitus.txt", "r", encoding="utf-8")
sisu = fail.read()
fail.close()

print(sisu)