
data.tambah(
     input("Masukkan NIM : "), 
     input("Masukkan Nama : "), 
     int(input("Nilai Tugas : ")), 
     int(input("Nilai UTS : ")), 
     int(input("Nilai UAS : "))
     )
     print("\nData berhasil ditambahkan")

elif menu == "u" or menu == "U":
        print("\nUbah Data")
        ubah = input("Masukkan Nama : ")
        if ubah in data.nama:
           no = data.nama.index(ubah)
           print("Masukkan Data Yang Baru : ")
           data.ubah(
               input("NIM : "),
               input("Nama : "),
               int(input("Nilai Tugas : ")),
               int(input("Nilai UTS : ")),
               int(input("Nilai UAS : "))
               )
        else:
            print(ubah, "tidak ada di dalam data")

elif menu == "h" or menu == "H":
        print("\nHapus Data")
        hapus = input("Masukkan Nama : ")
        if hapus in data.nama:
            no = data.nama.index(hapus)
            data.hapus()
            print("Data", hapus, "Berhasil dihapus")
        else:
            print(hapus, "tidak ada di dalam data")

def tulis():
     input("Masukkan NIM : "), 
     input("Masukkan Nama : "), 
     int(input("Nilai Tugas : ")), 
     int(input("Nilai UTS : ")), 
     int(input("Nilai UAS : "))
