
from model import daftar_nilai
from view import input_nilai
from view import view_nilai


while True:
 menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]:")
 if menu == "t" or menu == "T":
     input_nilai.tulis("pp")
 else:
     print("\nPerintah yang dimasukkan salah!\n")