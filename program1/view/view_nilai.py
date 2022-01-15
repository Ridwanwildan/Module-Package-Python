elif menu == "l" or menu == "L":
     print("\nDaftar Nilai")
     print("==========================================================================")
     print("| No  |          Nama           |    NIM    | TUGAS | UTS | UAS |  AKHIR |")
     print("==========================================================================")
     if len(data.nama) != 0:
         data.lihat()
     else:
         print("                         TIDAK ADA DATA                               ")
     print("==========================================================================")