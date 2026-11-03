height = int(input("Masukan Angka: "))
for row in range(0, height):
    for column in range(0, height - row):
        print("*",end=" ")
    print()