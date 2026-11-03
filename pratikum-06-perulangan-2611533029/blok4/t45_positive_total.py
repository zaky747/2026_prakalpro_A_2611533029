result = 0
x = 1
while x >= 0:
    x = int(input("Masukan Angka: "))
    if x < 0:
        break
    if x == 0:
        continue
    print("Positive number:", x)
    result += x
print("Total:", result)