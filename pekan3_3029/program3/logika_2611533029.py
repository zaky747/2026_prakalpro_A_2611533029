#memasukkan nilai boolean
a1_3029 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3029 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 = ", a1_3029)
print("A2 = ", a2_3029)

# Konjungsi: bernilai True jika keduanya True
hasil_3029 = a1_3029 and a2_3029
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_3029)

# Disjungsi: bernilai True jika salah satunya True
hasil_3029 = a1_3029 or a2_3029
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3029)

# Negasi A1: mambalikan nilai A1
hasil_3029 = not a1_3029
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3029)

# Negasi A2: membalikan nilai A2
hasil_3029 = not a2_3029
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3029)

# XOR: bernilai True jika Kedua nilai berbeda
hasil_3029 = a1_3029 != a2_3029
print("\nDisjungsi eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3029)