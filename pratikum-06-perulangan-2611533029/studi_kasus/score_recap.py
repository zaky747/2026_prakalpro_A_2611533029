PASS_SCORE = 60

jumlah_3029 = int(input("Number of students: "))
while jumlah_3029 < 1:
    print("Invalid student count!")
    jumlah_3029 = int(input("Number of students: "))

total_3029 = 0
lulus_3029 = 0
tertinggi_3029 = 0

for ke_3029 in range(1, jumlah_3029 + 1):
    print("Student", ke_3029)
    skor_3029 = int(input("Enter score: "))

    while skor_3029 < 0 or skor_3029 > 100:
        print("Invalid score!")
        skor_3029 = int(input("Enter score: "))

    total_3029 = total_3029 + skor_3029

    if skor_3029 >= PASS_SCORE:
        lulus_3029 = lulus_3029 + 1

    if skor_3029 > tertinggi_3029:
        tertinggi_3029 = skor_3029

rata_3029 = round(total_3029 / jumlah_3029, 2)

print("Total score:", total_3029)
print("Average score:", rata_3029)
print("Passed:", lulus_3029)
print("Highest score:", tertinggi_3029)