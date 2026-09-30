print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
ukuran_3029 = int(input("Masukkan ukuran skala jam pasir (N): "))
print()

lebar_3029 = 4 * ukuran_3029 + 5

print("#", end="")
for i_3029 in range(lebar_3029):
    print("=", end="")
print("#")

for baris_3029 in range(ukuran_3029, 0, -1):
    print("|", end="")
    print(" ", end="")                                  
    for spasi_3029 in range(2 * (ukuran_3029 - baris_3029)):
        print(" ", end="")
    for angka_3029 in range(baris_3029, 0, -1):        
        print(angka_3029, end=" ")
    print("<*>", end="")                               
    for angka_3029 in range(1, baris_3029 + 1):        
        print(" ", angka_3029, sep="", end="")
    for spasi_3029 in range(2 * (ukuran_3029 - baris_3029)):
        print(" ", end="")
    print(" ", end="")                                 
    print("|")

print("|", end="")
for spasi_3029 in range(2 * ukuran_3029 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3029 in range(2 * ukuran_3029 + 1):
    print(" ", end="")
print("|")

for baris_3029 in range(1, ukuran_3029 + 1):
    print("|", end="")
    print(" ", end="")
    for spasi_3029 in range(2 * (ukuran_3029 - baris_3029)):
        print(" ", end="")
    for angka_3029 in range(baris_3029, 0, -1):
        print(angka_3029, end=" ")
    print("<*>", end="")
    for angka_3029 in range(1, baris_3029 + 1):
        print(" ", angka_3029, sep="", end="")
    for spasi_3029 in range(2 * (ukuran_3029 - baris_3029)):
        print(" ", end="")
    print(" ", end="")
    print("|")

print("#", end="")
for i_3029 in range(lebar_3029):
    print("=", end="")
print("#")