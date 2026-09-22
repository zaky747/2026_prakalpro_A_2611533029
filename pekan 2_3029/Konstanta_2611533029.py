# Buat file dengan nama Konstanta_2611533029
# Program ini menggunakan konstanta untuk menghitun luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_3029

from typing import Final
PI: Final = 3.14
print("Pi: %f" % (PI))
jari_3029 = float(input("Masukkan nilai jari-jari: "))
luas_3029 = PI * jari_3029
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3029,luas_3029))