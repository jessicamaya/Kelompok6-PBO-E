import datetime
import eq_database

class PetugasModel():
    def __init__(self):
        self.database_var = eq_database.Helper_Database()
        self.database_var.buatDatabase()
        self.data_hewan_header = ['ID', 'Waktu Mulai', 'Username Petugas', 'Username Pelanggan', 'Nama Peliharaan', 
                                  'Nama Kategori', 'Biaya/hari', 'Total hari', 'Biaya total sekarang']
        self.data_pelanggan_header = ['No', 'Username Pelanggan', 'Transaksi Berlangsung', 'Nama Pelanggan']
        self.data_riwayat_header = ['ID', 'Waktu Mulai', 'Waktu Selesai', 'Username Petugas', 'Username Pelanggan', 'Nama Peliharaan', 
                                  'Nama Kategori', 'Biaya/hari', 'Total hari', 'Biaya total sekarang']

    #tambah data hewan

    def verifikasi_username(self, usernameInput):
        hasil = self.database_var.verifikasi_username(usernameInput)
        return hasil

    def verifikasi_hewan(self, usernameInput, hewanInput):
        hasil = self.database_var.verifikasi_hewan(usernameInput, hewanInput)
        return hasil

    def verifikasi_kategori(self, kategoriInput):
        hasil = self.database_var.verifikasi_kategori(kategoriInput)
        return hasil

    def tambah_data_hewan(self, usernamePetugas, usernameInput, input_hewan):
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hasil = self.database_var.tambah_data_hewan_ke_db(usernamePetugas, usernameInput, waktu, input_hewan)
        return hasil

    #tambah data pelanggan

    def verifikasi_username_kosong(self, usernameInput):
        hasil = self.database_var.verifikasi_username_kosong(usernameInput)
        return hasil

    def tambah_data_pelanggan(self, usernameInput, namaInput, passwordInput):
        hasil = self.database_var.tambah_data_pelanggan(usernameInput, namaInput, passwordInput)
        return hasil

    #hapus data hewwan

    def ambil_max_id_transaksi(self):
        hasil = self.database_var.ambil_max_id_transaksi()
        return hasil

    def hapus_hewan(self, pilih):
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hasil = self.database_var.hapus_hewan(waktu, pilih)
        return hasil
    
    #lihat data hewan

    def ambil_semua_data_hewan(self):
        self.hasil = self.database_var.ambil_semua_data_hewan()
        self.proses_data_total_bayar()
        return self.data_hewan_header, self.list_hasil
    
    def proses_data_total_bayar(self):
        list_hasil = []
        for baris in self.hasil:
            baris = list(baris)
            baris[1] = baris[1].strftime("%d-%m-%Y %H:%M:%S")
            beda_hari = baris[-1]
            mod_hari = beda_hari%24
            if beda_hari % 24 >= 12:
                baris[-1] = int((beda_hari-mod_hari)/24 + 1)
            elif beda_hari/24 < 1 and beda_hari % 24 < 12:
                baris[-1] = int(1)
            else:
                baris[-1] = int(beda_hari/24)
                (beda_hari-mod_hari)/24 + 1
            baris.append(baris[-1] * baris[-2])
            list_hasil.append(baris)

        self.list_hasil = list_hasil
        
    def ambil_username_data_hewan(self, usernameInput):
        self.list_cari = []
        self.data_hewan_header, self.list_hasil = self.ambil_semua_data_hewan()
        for baris in self.list_hasil:
            if usernameInput == baris[3]:
                self.list_cari.append(baris)
        
        return self.data_hewan_header, self.list_cari

    #lihat data pelanggan
    
    def ambil_semua_data_pelanggan(self):
        self.hasil = self.database_var.ambil_semua_data_pelanggan()
        self.proses_data_pelanggan()
        return self.data_pelanggan_header, self.list_hasil_pelanggan

    def proses_data_pelanggan(self):
        list_hasil_pelanggan = []
        nomor = 1
        for baris in self.hasil:
            baris = list(baris)
            baris.pop(-1)
            baris.insert(0, nomor)
            baris.insert(-1, self.cari_jumlah_transaksi(baris[1]))
            list_hasil_pelanggan.append(baris)
            nomor += 1

        self.list_hasil_pelanggan = list_hasil_pelanggan

    def cari_jumlah_transaksi(self, usernameInput):
        jumlah_transaksi = self.database_var.cari_jumlah_transaksi(usernameInput)
        return jumlah_transaksi

    #lihat data riwayat

    def ambil_semua_data_riwayat(self):
        self.hasil = self.database_var.ambil_semua_data_riwayat()
        self.proses_data_total_bayar_riwayat()
        return self.data_riwayat_header, self.list_hasil
    
    def proses_data_total_bayar_riwayat(self):
        list_hasil = []
        for baris in self.hasil:
            baris = list(baris)
            baris[1] = baris[1].strftime("%d-%m-%Y %H:%M:%S")
            baris[2] = baris[2].strftime("%d-%m-%Y %H:%M:%S")
            beda_hari = baris[-1]
            mod_hari = beda_hari%24
            if beda_hari % 24 >= 12:
                baris[-1] = int((beda_hari-mod_hari)/24 + 1)
            elif beda_hari/24 < 1 and beda_hari % 24 < 12:
                baris[-1] = int(1)
            else:
                baris[-1] = int(beda_hari/24)
                (beda_hari-mod_hari)/24 + 1
            baris.append(baris[-1] * baris[-2])
            list_hasil.append(baris)

        self.list_hasil = list_hasil
        





