import eq_database
import eq_trycatch
import login_model
import pelanggan_control
import petugas_control

class LoginController(eq_trycatch.TryCatcher):
    def __init__(self):
        super().__init__()
        self.loginModel = login_model.LoginModel()
        print()

    def tampilkan_menu_login_inputan(self):
        print(""" 
Pilihan menu :
1. Masukkan kredensial
2. Kembali""")
        pilih = 0
        pilih = self.check_int(1,2)
        print()
        if pilih == 1:
            print("="*10, "LOGIN", "="*10)
            self.usernameLogin = self.check_str("Masukkan username\t: ")
            self.__passwordLogin = self.check_str("Masukkan password\t: ")
            print()
            if self.loginModel.verifikasi_akun(self.loginSebagai, self.usernameLogin, self.__passwordLogin) == True:
                if self.loginSebagai == "Petugas":
                    petugas = petugas_control.PetugasController(self.usernameLogin)
                    print("\n")
                    petugas.tampilkan_menu_utama()
                elif self.loginSebagai == "Pelanggan":
                    pelanggan = pelanggan_control.PelangganController(self.usernameLogin)
                    print("\n")
                    pelanggan.tampilkan_menu_utama()

            elif self.loginModel.verifikasi_akun(self.loginSebagai, self.usernameLogin, self.__passwordLogin) == "Nodata":
                print("Data tidak ditemukan pada sistem.")
                self.tampilkan_menu_login_inputan()

            else:
                print("Password atau username salah. Silahkan coba login lagi.")
                self.tampilkan_menu_login_inputan()
                
        elif pilih == 2:
            self.tampilkan_menu_login()
        
    def tampilkan_menu_login(self):
        print(""" Pilihan menu :
1. Login Petugas
2. Login Pelanggan
3. Keluar""")
        pilih = self.check_int(1,3)
        if pilih == 1:
            self.loginSebagai = "Petugas"
            self.tampilkan_menu_login_inputan()
        elif pilih == 2:
            self.loginSebagai = "Pelanggan"
            self.tampilkan_menu_login_inputan()
        elif pilih == 3:
            exit()

    def tampilkan_menu_utama(self):
        """
        kelas ini digunakan untuk menampilkan menu utama.
        Menu utama bisa untuk petugas atau pelanggan, tergantung dari login.
        Apakah sebagai petugas, atau pelanggan.
        """
        raise NotImplementedError
    
if __name__=='__main__':
    login = LoginController()
    login.tampilkan_menu_login()
    
    
