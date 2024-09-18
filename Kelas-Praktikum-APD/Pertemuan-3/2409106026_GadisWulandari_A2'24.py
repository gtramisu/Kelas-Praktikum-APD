harga = int(input ("masukkan harga barang : "))
jumlah = int(input ("masukkan jumlah barang : "))
diskon = 0.20
harga_total = harga*jumlah

if harga > 100000 and jumlah >= 5:
    diskon_barang = harga_total*diskon
    harga_diskon = harga_total-diskon_barang
    print(f"harga diskon :{harga_diskon} ")
else:
    print ("anda telah mendapatkan diskon")




nilai = int(input ("masukkan nilai= "))

 if nilai > 100 :
    Print ("kondisi tidak memenuhi syarat")
 if nilai > 80 :
    if nilai >= 90 and nilai <= 100 :
        print ("nilai anda A+")
    if nilai >= 80 and nilai <= 89 :
       print ("nilai anda A-")
 if nilai >= 70 :
    if nilai >= 75 and nilai <= 79 :
       print ("nilai anda B+")
    if nilai >= 70 and nilai <= 74 :
       print ("nilai anda B-")
 else :
    print ("kondisi tidak memenuhi syarat")




    fitur = int(input("pilih fitur : "))
match fitur :
    case 1:
        a = int(input("Masukkan angka 1 : "))
        b = int(input("Masukkan angka 2 : "))
        c = a + b 
        print (f"hasil penjumlahan angka 1 dan angka 2 adalah {c}")
    case 2:
        a = int(input("Masukkan angka 1 : "))
        b = int(input("Masukkan angka 2 : "))
        c = a - b 
        print (f"hasil pengurangan angka 1 dan angka 2 adalah {c}")
    case 3:
        a = int(input("Masukkan angka 1 : "))
        b = int(input("Masukkan angka 2 : "))
        c = a * b 
        print (f"hasil perkalian angka 1 dan angka 2 adalah {c}")
    case 4:
        a = int(input("Masukkan angka 1 : "))
        b = int(input("Masukkan angka 2 : "))
        c = a / b 
        print (f"hasil pembagian angka 1 dan angka 2 adalah {c}")





jenis_kelamin = input("Masukkan jenis kelamin anda (L/P): ")

hasil = ("Jenis Kelamin Laki-Laki" if jenis_kelamin == "L" else "Jenis Kelamin Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui")

print(hasil)
    