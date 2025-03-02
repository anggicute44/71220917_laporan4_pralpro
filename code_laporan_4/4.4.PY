try:
    sisi1 = float(input("Masukkan sisi 1: "))
    sisi2 = float(input("Masukkan sisi 2: "))
    sisi3 = float(input("Masukkan sisi 3: "))

    if sisi1 == sisi2 == sisi3:
        print("3 sisi sama")
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        print("2 sisi sama")
    else:
        print("Tidak ada yang sama")
except ValueError:
    print("Input harus berupa bilangan")
