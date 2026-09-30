tinggi_3029 = int(input("Masukkan tinggi segitiga: "))

for i_3029 in range(1, tinggi_3029 + 1):
    print(" " * (tinggi_3029 - i_3029), end="")  # cetak spasi
    for j_3029 in range(1,i_3029 + 1):
        print("*", end=" ")
    print()  # pindah ke baris berikutnya