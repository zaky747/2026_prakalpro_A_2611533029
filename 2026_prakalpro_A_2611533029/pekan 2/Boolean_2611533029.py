# Buat file dengan nama Boolean_NIM.PY
#Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# deklarasi variabel dengan tipe data Boolean 
is_lulus_3029 = True
is_cumlaude_3029 = True

# menggunakan Boolean
nilai_3029 = 85
batas_lulus_3029 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_3029 = nilai_3029 >= batas_lulus_3029  # Hasilnya akan true

print("=== check kelulusan ===")
print("Nilai:", nilai_3029)
print("Apakah Lulus?:", status_kelulusan_3029)
if is_lulus_3029 and is_cumlaude_3029:
    print("selamat, Anda lulus dengan predikat cum laude!")