# for j in range(2,12,2):
#     print("halo")
# print("hai")

# print("Menu Rumah Makan Informatika 24: ")
# print("--------------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
# for i in simpan:
#     print(i)

# print("Menu Rumah Makan Informatika 24: ")
# print("--------------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
# for i, menu in enumerate(simpan,start=1):
#     print(f"{i}. {menu}")

# print("Menu Rumah Makan Informatika 24: ")
# print("--------------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
# for i in range(len(simpan)):
#     print(f"{i+1}. {simpan[i]}")

# for i in range(1, 4):
#    for j in range(1, 4):
#        print(f"{i} x {j} = {i * j}")
#    print()

# makanan = ["mie","sop","bakso"]
# minuman = ["es teh", "air putih","es jeruk"]

# for i in makanan:
#     for j in minuman:
#        print(f"{i} & {j}")

# while True:
#     print("hello word")

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}")

# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya' or jawab == 'Ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total perulangan: {hitung}")

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# i = 0
# while i < 5:
#     print(i)
#     break
#     i += 1

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih Ingin Mengulang? ")
#     if ulang == "tidak" or ulang =="Tidak":
#         print("oke kita udahan")
#         break
# print(f"Total Perulangan: {hitung}")

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih Ingin Lanjut? ")
#     if ulang == "y" or ulang =="Y":
#         print("oke kita lanjut")
#         continue

# print(f"Total perulangan: {hitung}")

# print("Daftar bilangan ganjil dari 1-10")
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# total = 0
# while True:
#     angka = int(input("masukkan angka positif (input negatif jika ingin berhenti: "))
#    if angka < 0:
#         break
# total +=angka

# print(f"jumlah total adalah:",total)

# range_maks = int(input("range maksimal : "))
# hitung prima = 0
#   for angka in range(1, range_maks):

# Meminta input dari pengguna untuk range maksimal
# range_maksimal = int(input("Masukkan range maksimal: "))

# Inisialisasi variabel untuk menyimpan jumlah bilangan prima
# hitung_prima = 0

# Loop untuk memeriksa setiap angka dari 1 hingga range_maksimal
# for angka in range(1, range_maksimal):
#     angka += 1
#     apakah_prima = True  # Anggap angka tersebut prima

# Cek apakah angka memiliki pembagi selain 1 dan dirinya sendiri
#     for i in range(2, angka):
#         if angka % i == 0:
#             apakah_prima = False  # Jika ada pembagi, bukan bilangan prima
# print(f"{angka} bukan prima")
#            break
# Jika angka tersebut prima, tambahkan jumlah hitung_prima
#    if apakah_prima == True:
#        print(f"{angka} prima")
#        hitung_prima += 1

# output
# print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")
