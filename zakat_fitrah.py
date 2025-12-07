jumlah_minimal = 2.5 # dalam satuan kg beras

try:
    jumlah_orang_input = input("Masukkan jumlah orang dalam keluarga Anda: ")
    
    if not jumlah_orang_input or jumlah_orang_input.strip() == "":
        print("Harap masukkan jumlah orang")
        exit()
    
    jumlah_orang = int(jumlah_orang_input)
    
    if jumlah_orang <= 0:
        print("Jumlah orang harus lebih dari 0")
        exit()
        
except ValueError:
    print("Harap masukkan angka yang valid")
    exit()

jumlah_zakat = float(jumlah_minimal * jumlah_orang)

print("Jadi jumlah zakat yang wajib dikeluarkan dari Keluarga Anda adalah", jumlah_zakat, "kg")