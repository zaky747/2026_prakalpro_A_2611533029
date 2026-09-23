("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_3029 = input("Masukkan Nama Pengunjung        : ")
umur_3029 = int(input("Input umur anda                 : "))
sim_c_3029 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].strip().lower()

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")
paket_3029 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3029 = int(input("Masukkan jumlah tiket           : "))
if jumlah_tiket_3029 <= 0:
    print("Jumlah tiket tidak valid!")
    exit()
member_3029 = input("Apakah Anda member? (y/t)       : ")[0].strip().lower()
promo_3029 = input("Apakah kode promo valid? (y/t)  : ")[0].strip().lower()

wahana_3029 = ""
harga_satuan_3029 = 0

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
match paket_3029:
    case 1: # Wahana Safari Rimba
        if umur_3029 >= 10:
            print("Anda sudah dewasa dan boleh mengendarai Wahana Safari Rimba sendiri.")
        else:
            print("Anda wajib didampingi orang tua.")
        harga_satuan_3029 = 50000
    case 2: # Wahana Arung Jeram
        if umur_3029 >= 15:
            print("Anda sudah dewasa dan boleh mengendarai Wahana Arung Jeram sendiri.")
        else:
            print("Anda wajib didampingi orang tua.")
        harga_satuan_3029 = 75000
    case 3: # Wahana Motor ATV Ekstrim
        if umur_3029 >= 17 and sim_c_3029 == 'y':
            print("Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
        elif umur_3029 >= 17 and sim_c_3029 != 'y':
            print("Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_3029 < 17 and sim_c_3029 == 'y':
            print("Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Anda belum cukup umur dan tidak boleh bawa motor ATV.")
        harga_satuan_3029 = 120000
    case 4: # Wahana Roller Coaster Kilat
        if umur_3029 >= 17:
            print("Anda sudah dewasa dan boleh mengendarai Wahana Roller Coaster Kilat sendiri.")
        else:
            print("Anda wajib didampingi orang tua.")
        harga_satuan_3029 = 100000
    case 5: # Wahana All-Access VIP
        if umur_3029 >= 17 and sim_c_3029 == 'y':
            print("Anda sudah dewasa dan boleh mengendarai semua wahana sendiri.")
        elif umur_3029 >= 17 and sim_c_3029 != 'y':
            print("Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_3029 < 17 and sim_c_3029 == 'y':
            print("Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Anda belum cukup umur dan tidak boleh bawa motor ATV.")
        harga_satuan_3029 = 220000
    case _: 
        print("Paket wahana tidak valid!")
        exit()

diskon_3029 = 0
if harga_satuan_3029 * jumlah_tiket_3029 >= 200000:
    diskon_3029 += 10
if member_3029 in ["y","ya"]:
    diskon_3029 += 5
if promo_3029 in ["y","ya"]:
    diskon_3029 += 15
if jumlah_tiket_3029 >= 5:
    diskon_3029 += 5

nominal_3029 = harga_satuan_3029 * jumlah_tiket_3029
nominal_diskon_3029 = nominal_3029 * (diskon_3029 / 100)
total_bayar_3029 = nominal_3029 - nominal_diskon_3029
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {nominal_3029:,}")
if nominal_3029 > 300000: 
    print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
print(f"Total Diskon     : {diskon_3029}% (Rp {int(nominal_diskon_3029):,})")
print(f"Total Bayar      : Rp {int(total_bayar_3029):,}")
print("Catatan Layanan  : Terima kasih telah berkunjung.")
print("Program Selesai")