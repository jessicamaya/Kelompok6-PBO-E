import datetime
import eq_database

class PelangganModel():
    def __init__(self):
        self.database_var = eq_database.Helper_Database()
        self.database_var.buatDatabase()
        self.data_hewan_header = ['ID', 'Waktu Mulai', 'Username Petugas', 'Username Pelanggan', 'Nama Peliharaan', 
                                  'Nama Kategori', 'Biaya/hari', 'Total hari', 'Biaya total sekarang']

        self.data_riwayat_header = ['ID', 'Waktu Mulai', 'Waktu Selesai', 'Username Petugas', 'Username Pelanggan', 'Nama Peliharaan', 
                                  'Nama Kategori', 'Biaya/hari', 'Total hari', 'Biaya total sekarang']

    def ambil_username_data_hewan(self, usernameInput):
        self.list_hasil = []
        self.list_cari = self.database_var.ambil_semua_data_hewan_username(usernameInput)
        for baris in self.list_cari:
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
            self.list_hasil.append(baris)
        
        return self.data_hewan_header, self.list_hasil

    def ambil_username_data_riwayat(self, usernameInput):
        self.hasil = self.database_var.ambil_username_data_riwayat(usernameInput)
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
