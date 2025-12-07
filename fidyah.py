minimal_beras = 0.675

jenis_pembayaran = input("Jenis pembayaran Anda: ").strip().lower()

if jenis_pembayaran == "beras":
    jumlah_hari_tidak_puasa = int(input("Jumlah hari Anda tidak puasa: "))
    jumlah_fidyah = jumlah_hari_tidak_puasa * minimal_beras
    print("Jadi Anda harus membayar fidyah besar sebesar", round(jumlah_fidyah), "kg beras")
elif jenis_pembayaran == "uang":
    jumlah_hari_tidak_puasa = int(input("Jumlah hari Anda tidak puasa: "))
    jumlah_harga_beras = 16000 * 0.675
    jumlah_fidyah = jumlah_hari_tidak_puasa * jumlah_harga_beras
    print("Jadi Anda harus membayar fidyah sebesar Rp ", round(jumlah_fidyah))
else:
    print("Masukan tidak valid")

print(20000-15990)