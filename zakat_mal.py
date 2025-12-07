
# optimized code
def rupiah(x):
    return f"Rp {x:,.0f}".replace(",", ".")

nisab = 85000000

jenis_harta = input("Masukkan jenis harta: ").strip().lower()

if jenis_harta == "emas":
    harga_satuan = int(input("Harga satuan emas (Rp): "))
    jumlah = int(input("Jumlah emas dalam gram: "))
    nilai_harta = harga_satuan * jumlah
else:
    nilai_harta = int(input("Masukkan nilai harta Anda (Rp): "))

if nilai_harta < 0:
    print("Masukan tidak valid")
elif nilai_harta < nisab:
    print("Belum wajib membayar zakat maal.")
elif nilai_harta >= nisab:
    jumlah_zakat = 0.025 * nilai_harta
    print("Anda sudah wajib membayar zakat maal!")
    print("Jumlah zakat yang harus dibayar: ", rupiah(round(jumlah_zakat)))


# old code
# nisab = 85000000

# jenis_harta = input("Masukkan jenis harta: ").strip().lower()

# if jenis_harta == "emas":
#     harga_satuan = int(input("Harga satuan (Rp): "))
#     jumlah = int(input("Jumlah emas dalam gram: "))

#     if harga_satuan * jumlah < nisab:
#         print("Belum wajib membayar zakat maal!")
#     elif harga_satuan * jumlah >= nisab:
#         print("Anda sudah wajib membayar zakat maal!")
#         jumlah_zakat = (2.5/100) * (harga_satuan * jumlah)
#         print("Jumlah zakat yang harus dibayar", round(jumlah_zakat))
# else:
#     nilai_langsung = int(input("Masukkan nilai harta Anda: "))

#     if nilai_langsung < nisab:
#         print("Belum wajib membayar zakat maal!")
#     elif nilai_langsung >= nisab:
#         print("Anda sudah wajib membayar zakat maal!")
#         jumlah_zakat = (2.5/100) * nilai_langsung
#         print("Jumlah zakat yang harus dibayar: ", round(jumlah_zakat))