list_buah = ["Apel", "Semangka", "Anggur"]

print("--OPERASI--")
print("Create")
print("Read")
print("Get_by_name")
print("Update")
print("Delete")

operasi = input("Operasi apa yang ingin Anda lakukan? ").capitalize()

if operasi == "Read":
    print("List buah:", list_buah)
elif operasi == "Create":
    masukan = input("Masukkan buah Anda: ")
    list_buah.append(masukan)
    print("Selamat operasi Anda berhasil. List buah Anda sekarang:", list_buah)
elif operasi == "Delete":
    masukan = input("Buah apa yang ingin dihapus? ").capitalize()
    if masukan not in list_buah:
        print("masukan tidak ada di list")
    else:
        list_buah.remove(masukan)
        print("Selamat operasi Anda berhasil. List buah Anda sekarang:", list_buah)
elif operasi == "Get_by_name":
    masukan = input("Masukkan buah Anda: ").capitalize()
    if masukan in list_buah:
        print(masukan)
    else:
        print("masukan Anda tidak ada di list")
elif operasi == "Update":
    index = int(input("Masukkan indexnya: "))
    if index < 0 or index > len(list_buah):
        print("Index Anda melebihi range list")
    else:
        print(list_buah[index])
        masukan = input("Apa perubahan Anda? ").capitalize()
        list_buah[index] = masukan
        print("Selamat operasi Anda berhasil. List buah sekarang", list_buah)
else:
    print("Masukan tidak valid")