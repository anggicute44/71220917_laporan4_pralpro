try:
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        hari = 31
    elif bulan in [4, 6, 9, 11]:
        hari = 30
    elif bulan == 2:
        hari = 29  
    else:
        raise ValueError("Bulan tidak valid")
    print(f"Jumlah hari: {hari}")
except ValueError as err:
    print("Bulan yang anda masukkan tidak valid.", err)