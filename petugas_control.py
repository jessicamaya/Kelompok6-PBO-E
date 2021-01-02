import eq_trycatch
import login_control
import petugas_model

class PetugasController(eq_trycatch.TryCatcher):
    def __init__(self, username):
        self.username = username
        print("Selamat datang, {}. Anda berhasil login.".format(self.username))
        super().__init__()
        self.petugasModel = petugas_model.PetugasModel()
        
    def tampilkan_menu_utama(self):
        print("""Masukkan angka pilihan menu anda dari daftar berikut
1. Tambahkan data (data pelanggan, data hewan)
2. Hapus hewan yang dirawat
3. Lihat hewan yang dirawat atau data pelanggan
4. Lihat riwayat penitipan
5. Logout
6. Berhenti""")
        pilih = self.check_int(1,6)
        if pilih == 1:
            self.tambah_data()
            self.tampilkan_menu_utama()
        elif pilih == 2:
            self.hapus_hewan()
            self.tampilkan_menu_utama()
        elif pilih == 3:
            self.lihat_hewan()
            self.tampilkan_menu_utama()
        elif pilih == 4:
            self.lihat_riwayat()
            self.tampilkan_menu_utama()
        elif pilih == 5:
            login = login_control.LoginController()
            login.tampilkan_menu_login()
        elif pilih == 6:
            exit()
    
#Menu1 : Tambah hewan

    def tambah_data(self):
        print("""Masukkan angka pilihan menu anda dari daftar berikut
1. Tambahkan data hewan
2. Tambahkan data pelanggan
3. Kembali ke menu utama""")
        pilih = self.check_int(1,3)
        if pilih == 1:
            self.tambah_hewan()
            self.tambah_data()
        elif pilih == 2:
            self.tambah_pelanggan()
            self.tambah_data()
        elif pilih == 3:
            self.tampilkan_menu_utama()

    def tambah_hewan(self):
        input_hewan = []
        tambah_lagi = True
        while True:
            usernameInput = self.check_str("Masukkan username pelanggan : ")
            verif = self.petugasModel.verifikasi_username(usernameInput)
            if verif == True:
                break
            elif verif == False:
                print("Username tidak ada di data kami. Mohon coba lagi")

        while tambah_lagi == True:
            while True:
                hewanInput = self.check_str("Masukkan nama hewan : ")
                verif = self.petugasModel.verifikasi_hewan(usernameInput, hewanInput)
                if verif == True:
                    break
                elif verif == False:
                    print("Hewan sedang dititipkan sekarang.")
            
            while True:
                kategoriInput = self.check_str("Masukkan kategori hewan : ")
                verif = self.petugasModel.verifikasi_kategori(kategoriInput)
                if verif == True:
                    break
                elif verif == False:
                    print("Kategori ini tidak ditemukan pada data kami. Mohon coba lagi")
    
            input_hewan.append([hewanInput, kategoriInput])
            print("""Apakah anda ingin menambahkan peliharaan lain dari pelanggan ini?
1. Ya
2. Tidak""")
            input_lagi = self.check_int(1,2)
            if input_lagi == 2:
                break

        sukses = self.petugasModel.tambah_data_hewan(self.username, usernameInput, input_hewan)
        if sukses == True:
            print("Data hewan sukses ditambahkan.\n")
        elif sukses == False:
            print("Terjadi kesalahan. Coba lagi.\n")

    def tambah_pelanggan(self):
        while True:
            usernameInput = self.check_str("Masukkan username pelanggan : ")
            verif = self.petugasModel.verifikasi_username_kosong(usernameInput)
            if verif == True:
                break
            elif verif == False:
                print("Username tidak tersedia. Mohon coba lagi")
        
        namaInput = self.check_str("Masukkan nama lengkap pelanggan : ")
        passwordInput = self.check_str("Masukkan password pelanggan : ")

        sukses = self.petugasModel.tambah_data_pelanggan(usernameInput, namaInput, passwordInput)
        if sukses == True:
            print("Data pelanggan sukses ditambahkan.\n")
        elif sukses == False:
            print("Terjadi kesalahan. Coba lagi.")
    
#Menu2 : Hapus hewan

    def hapus_hewan(self):
        #hapus hewan dengan caraa pasang date dikembalikan ke pemiliknya ya. jangan lupa bayarnya juga dicatet!
        self.lihat_semua_hewan()
        pilih = self.check_int(1,self.petugasModel.ambil_max_id_transaksi(), "Masukkan ID yang ingin dihapus : ")
        hasil = self.petugasModel.hapus_hewan(pilih)
        if hasil == True:
            print("Data hewan telah berhasil dihapus\n")


#Menu3 : Lihat hewan & pelanggan

    def lihat_hewan(self):
        print("""Masukkan angka pilihan menu anda dari daftar berikut
1. Lihat semua hewan yang sedang dititipkan
2. Lihat hewan yang dititipkan oleh salah satu pelanggan
3. Lihat semua data pelanggan
4. Kembali ke menu utama""")
        pilih = self.check_int(1,4)
        if pilih == 1:
            self.lihat_semua_hewan()
            self.lihat_hewan()
        elif pilih == 2:
            self.lihat_username_hewan()
            self.lihat_hewan()
        elif pilih == 3:
            self.lihat_semua_pelanggan()
            self.lihat_hewan()
        elif pilih == 4:
            self.tampilkan_menu_utama()

    def lihat_semua_hewan(self):
        header, hasil = self.petugasModel.ambil_semua_data_hewan()

        print("{:^4} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*header))
        for i in hasil:
            print("{:^4} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*i))
            
    def lihat_username_hewan(self):
        usernameInput = self.check_str("Masukkan username yang dicari : ")
        header, hasil = self.petugasModel.ambil_username_data_hewan(usernameInput)

        print("{:^4} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*header))
        for i in hasil:
            print("{:^4} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*i))

    def lihat_semua_pelanggan(self):
        header, hasil = self.petugasModel.ambil_semua_data_pelanggan()

        print("{:<8} {:^25} {:^25} {:<50} ".format(*header))
        for i in hasil:
            print("{:<8} {:<25} {:^25} {:<50}".format(*i))

#Menu4 : Lihat riwayat
    
    def lihat_riwayat(self):
        header, hasil = self.petugasModel.ambil_semua_data_riwayat()

        print("{:^4} {:^24} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*header))
        for i in hasil:
            print("{:^4} {:^24} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*i))



        


