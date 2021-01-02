import eq_trycatch
import login_control
import pelanggan_model

class PelangganController(eq_trycatch.TryCatcher):
    def __init__(self, username):
        self.username = username
        print("Selamat datang, {}. Anda berhasil login.".format(self.username))
        super().__init__()
        self.pelangganModel = pelanggan_model.PelangganModel()
        
    def tampilkan_menu_utama(self):
        print("""Masukkan angka pilihan menu anda dari daftar berikut
1. Lihat hewan yang dirawat
2. Lihat riwayat penitipan
3. Logout
4. Berhenti""")
        pilih = self.check_int(1,4)
        if pilih == 1:
            self.lihat_hewan_username()
            self.tampilkan_menu_utama()
        elif pilih == 2:
            self.lihat_riwayat_username()
            self.tampilkan_menu_utama()
        elif pilih == 3:
            login = login_control.LoginController()
            login.tampilkan_menu_login()
        elif pilih == 4:
            exit()

    def lihat_hewan_username(self):
        header, hasil = self.pelangganModel.ambil_username_data_hewan(self.username)

        print("{:^4} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*header))
        for i in hasil:
            print("{:^4} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*i))

    def lihat_riwayat_username(self):
        header, hasil = self.pelangganModel.ambil_username_data_riwayat(self.username)

        print("{:^4} {:^24} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*header))
        for i in hasil:
            print("{:^4} {:^24} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*i))



