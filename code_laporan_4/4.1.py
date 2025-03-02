# #3.1

# def tesprima(n, i=2):
#     if n < 2:
#         return False
#     elif i * i > n:
#         return True
#     elif n % i == 0:
#         return False
#     return tesprima(n, i + 1)

# def prima():
#     num = input("Masukkan bilangan bulat positif: ")

#     if num.isdigit():
#         num = int(num)
#         if tesprima(num):
#             print(f"{num}  bilangan prima.")
#         else:
#             print(f"{num} bukan bilangan prima.")
#     else:
#         print("GAK VALID.")
# prima()

# #3.2
# def akar():
#     koef_a = input("Masukkan koefisien a: ")
#     koef_b = input("Masukkan koefisien b: ")
#     koef_c = input("Masukkan koefisien c: ")

#     if koef_a.replace(".", "", 1).isdigit() and koef_b.replace(".", "", 1).isdigit() and koef_c.replace(".", "", 1).isdigit():
#         koef_a, koef_b, koef_c = float(koef_a), float(koef_b), float(koef_c)

#         if koef_a == 0:
#             print("Ini bukan persamaan kuadrat. Koefisien 'a' tidak boleh 0.")
#         else:
#             diskriminan = koef_b**2 - 4 * koef_a * koef_c
#             if diskriminan > 0:
#                 print("Akar Real dan Berlainan.")
#             elif diskriminan == 0:
#                 print("Akar Real dan Kembar.")
#             else:
#                 print("Akar Imajiner/Tidak Real.")
#     else:
#         print("Input tidak valid. Masukkan angka.")

# akar()


#3.3
def rekursif(n):
    return 1 if n == 0 else n * rekursif(n - 1)

def faktorial():
    n = input("Masukkan bilangan bulat positif: ")

    if n.isdigit():
        n = int(n)
        if n < 0:
            print("Bilangan tidak boleh negatif.")
        else:
            print(f"Faktorial dari {n} adalah {rekursif(n)}")
    else:
        print("Input tidak valid. Masukkan bilangan bulat positif.")

faktorial()
