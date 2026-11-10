fail = open("nimed.txt", "r", encoding="utf-8")
read = fail.readlines()
fail.close()

print("Failis on", len(read), "nime.")