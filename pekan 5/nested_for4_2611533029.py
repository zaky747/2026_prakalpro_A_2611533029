# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam pytohn
# Nama variabel ditambah 4 digit nim terakhir c_3029ontoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_3029 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3029 % 2 != 0:
    print("Tinggi pola harus bilangan genap.")
else:
    a_3029 = tinggi_3029
    c_3029 = a_3029
    lebar_3029 = (2 * tinggi_3029) - 2

    for i_3029 in range(1, tinggi_3029 + 1):
        b_3029 = c_3029 + 1

        for j_3029 in range(1, lebar_3029 + 1):

            # Baris atas dan bawah
            if i_3029 == 1 or i_3029 == tinggi_3029:
                if j_3029 == 1 or j_3029 == lebar_3029:
                    print("#", end="")
                else:
                    print("*", end="")
            # Baris isi
            else:
                if j_3029 == 1 or j_3029 == lebar_3029:
                    print("|", end="")
                else:
                    if j_3029 == c_3029:
                        print("<", end="")
                    elif j_3029 == b_3029:
                        print(">", end="")
                    elif j_3029 == (lebar_3029 - c_3029):
                        print("<", end="")
                    elif j_3029 == (lebar_3029 - c_3029 + 1):
                        print(">", end="")
                    elif j_3029 > b_3029 and j_3029 < (lebar_3029 - c_3029):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # logika asli java
        a_3029 -= 2
        if a_3029 <= 0:
            c_3029 = -a_3029 + 2
        else:
            c_3029 = a_3029