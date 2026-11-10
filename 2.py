with open("tervitus.txt", "r", encoding="utf-8") as fail:
    for nr, rida in enumerate(fail, start=1):
        print(f"{nr}: {rida.strip()}")