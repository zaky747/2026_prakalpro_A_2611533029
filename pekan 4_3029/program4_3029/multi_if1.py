# Buat file dengan nama multi_if1.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_3029 = int(input("Input umur anda: "))
sim_3029 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_3029 >= 17 and sim_3029 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_3029 >= 17 and sim_3029 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_3029 < 17 and sim_3029 != 'y':
    print("Anda Belum Cukup Umur bawa motor")

if umur_3029 < 17 and sim_3029 == 'y':
    print("Anda Belum Cukup Umur punya SIM") 