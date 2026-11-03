# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam pytohn
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_3029 = int(input("Masukkan jumlah perulangan: "))

jumlah_3029 = 0
for i_3029 in range(1,ulang_3029+1):
    print(i_3029,end=" ")
    jumlah_3029 = jumlah_3029 + i_3029

    if i_3029 < ulang_3029:
        print(" + ",end=" ")
    else:
        print(" = ",jumlah_3029,end=" ")
print()
print("Jumlah =",jumlah_3029)