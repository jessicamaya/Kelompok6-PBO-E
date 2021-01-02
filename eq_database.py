import mysql.connector

class Helper_Database():
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
    )
    
    def buatDatabase(self):
        cursor = self.db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS daycare;"
        cursor.execute(sql)
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="daycare"
        )
        
    def is_connected(self):
        if self.db.is_connected():
            return True
        
    def buatTabel(self):
        cursor = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS tb_Pelanggan (
                usernamePelanggan varchar(15) PRIMARY KEY,
                nama VARCHAR(40),
                password VARCHAR(15)
                );"""
        cursor.execute(sql)

        cursor = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS tb_Petugas (
                usernamePetugas varchar(15) PRIMARY KEY,
                nama VARCHAR(255),
                password VARCHAR(255)
                );"""
        cursor.execute(sql)

        cursor = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS tb_Transaksi (
                idTransaksi BIGINT AUTO_INCREMENT PRIMARY KEY,
                waktuTransaksi DATETIME NOT NULL,
                waktuPengembalian DATETIME NULL,
                usernamePetugas VARCHAR(15),
                usernamePelanggan VARCHAR(15),
                FOREIGN KEY (usernamePetugas) REFERENCES tb_Petugas(usernamePetugas),
                FOREIGN KEY (usernamePelanggan) REFERENCES tb_Pelanggan(usernamePelanggan)
                );"""
        cursor.execute(sql)

        cursor = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS tb_KategoriHewan(
                idKategori BIGINT AUTO_INCREMENT PRIMARY KEY,
                namaKategori VARCHAR(255),
                biaya float
        );"""
        cursor.execute(sql)

        cursor = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS tb_DetailTransaksi(
                idDetailTransaksi BIGINT AUTO_INCREMENT PRIMARY KEY,
                idTransaksi BIGINT,
                idKategori BIGINT,
                namaPeliharaan VARCHAR(20),
                FOREIGN KEY (idTransaksi) REFERENCES tb_Transaksi(idTransaksi),
                FOREIGN KEY (idKategori) REFERENCES tb_KategoriHewan(idKategori)
            );"""
        cursor.execute(sql)
        self.db.commit()

#database helper login

    def verifikasi_akun(self, loginSebagai, usernameLogin, __passwordLogin):
        if loginSebagai == "Petugas":
            cursor = self.db.cursor()
            sql = """SELECT password from tb_petugas where usernamePetugas = %s"""
            val = (usernameLogin,)
            cursor.execute(sql,val)

        elif loginSebagai == "Pelanggan":
            cursor = self.db.cursor()
            sql = """SELECT password from tb_pelanggan where usernamePelanggan = %s"""
            val = (usernameLogin,)
            cursor.execute(sql,val)

        hasil = cursor.fetchall()

        if hasil == []:
            return "Nodata"
        elif __passwordLogin == hasil[0][0]:
            return True
        else:
            return False

#database helper petugas

    def verifikasi_username(self, usernameInput):
        cursor = self.db.cursor()
        sql = """SELECT usernamePelanggan from tb_pelanggan where usernamePelanggan = %s"""
        val = (usernameInput,)
        cursor.execute(sql,val)

        hasil = cursor.fetchall()
        if hasil == []:
            return False
        else:
            return True

    def verifikasi_hewan(self, usernameInput, hewanInput):
        cursor = self.db.cursor()
        sql = """SELECT dt.namaPeliharaan FROM tb_transaksi t join tb_detailtransaksi dt
on t.idTransaksi = dt.idTransaksi
where t.usernamePelanggan = %s and t.waktuPengembalian is NULL"""
        val = (usernameInput,)
        cursor.execute(sql,val)

        hasil = cursor.fetchall()
        for i in range(0,len(hasil),1):
            if hasil[i][0].lower() == hewanInput.lower():
                return False
        return True

    def verifikasi_kategori(self,kategoriInput):
        cursor = self.db.cursor()
        sql = """SELECT namaKategori FROM tb_kategorihewan"""
        cursor.execute(sql)

        hasil = cursor.fetchall()
        for i in range(0,len(hasil),1):
            if hasil[i][0].lower() == kategoriInput.lower():
                return True
        return False

    def tambah_data_hewan_ke_db(self, usernamePetugas, usernameInput, waktu, input_hewan):
        cursor = self.db.cursor()
        sql = """INSERT INTO tb_transaksi (waktuTransaksi, waktuPengembalian, usernamePetugas, usernamePelanggan) 
                 VALUES (%s, NULL, %s, %s)"""
        val = (waktu, usernamePetugas, usernameInput)
        cursor.execute(sql,val)
        self.db.commit()

        for baris in input_hewan:
            cursor = self.db.cursor()
            sql = """INSERT INTO tb_detailtransaksi (idTransaksi, idKategori, namaPeliharaan) 
                    VALUES ((SELECT max(idTransaksi) FROM tb_transaksi) , (SELECT idKategori FROM tb_kategorihewan
                    where namaKategori = %s), %s)"""
            val = (baris[1], baris[0])
            cursor.execute(sql,val)
            self.db.commit()
        return True

    def verifikasi_username_kosong(self, usernameInput):
        cursor = self.db.cursor()
        sql = """SELECT usernamePelanggan from tb_pelanggan where usernamePelanggan = %s"""
        val = (usernameInput,)
        cursor.execute(sql,val)

        hasil = cursor.fetchall()
        if hasil == []:
            return True
        else:
            return False
    
    def tambah_data_pelanggan(self, usernameInput, namaInput, passwordInput):
        cursor = self.db.cursor()
        sql = """insert INTO tb_pelanggan VALUE (%s, %s, %s)"""
        val = (usernameInput, namaInput, passwordInput)
        cursor.execute(sql,val)
        self.db.commit()
        return True

#database hapus hewan

    def ambil_max_id_transaksi(self):
        cursor = self.db.cursor()
        sql = """SELECT max(idTransaksi) FROM tb_transaksi"""
        cursor.execute(sql)

        hasil = cursor.fetchall()
        return hasil[0][0]

    def hapus_hewan(self, waktuPengembalian, id_transaksi):
        cursor = self.db.cursor()
        sql = """UPDATE tb_transaksi
SET waktuPengembalian = %s
WHERE idTransaksi = %s"""
        val = (waktuPengembalian, id_transaksi)
        cursor.execute(sql,val)
        self.db.commit()
        return True

#database lihat hewan

    def ambil_semua_data_hewan(self):
        cursor = self.db.cursor()
        sql = """SELECT t.idTransaksi, t.waktuTransaksi, t.usernamePetugas, t.usernamePelanggan, 
                 dt.namaPeliharaan, k.namaKategori, k.biaya,
                 TIMESTAMPDIFF(HOUR, t.waktuTransaksi, NOW())
                 FROM tb_transaksi t join tb_detailtransaksi dt
                 on t.idTransaksi = dt.idTransaksi join tb_kategorihewan k
                 on dt.idKategori = k.idKategori
                 WHERE t.waktuPengembalian is NULL
                 ORDER BY t.idTransaksi asc
                 """
        cursor.execute(sql)
        hasil = cursor.fetchall()
        return hasil

#database lihat pelanggan

    def ambil_semua_data_pelanggan(self):
        cursor = self.db.cursor()
        sql = """SELECT * from tb_pelanggan"""
        cursor.execute(sql)
        hasil = cursor.fetchall()
        return hasil

    def cari_jumlah_transaksi(self, usernameInput):
        cursor = self.db.cursor()
        sql = """SELECT count(idTransaksi)
from tb_transaksi
where usernamePelanggan = %s"""
        val = (usernameInput,)
        cursor.execute(sql,val)

        hasil = cursor.fetchall()
        return hasil[0][0]

#database lihat riwayat

    def ambil_semua_data_riwayat(self):
        cursor = self.db.cursor()
        sql = """SELECT t.idTransaksi, t.waktuTransaksi, t.waktuPengembalian, t.usernamePetugas, t.usernamePelanggan, 
                 dt.namaPeliharaan, k.namaKategori, k.biaya,
                 TIMESTAMPDIFF(HOUR, t.waktuTransaksi, t.waktuPengembalian)
                 FROM tb_transaksi t join tb_detailtransaksi dt
                 on t.idTransaksi = dt.idTransaksi join tb_kategorihewan k
                 on dt.idKategori = k.idKategori
                 WHERE t.waktuPengembalian is not NULL
                 ORDER BY t.idTransaksi asc
                 """
        cursor.execute(sql)
        hasil = cursor.fetchall()
        return hasil

#database lihat hewan pelanggan

    def ambil_semua_data_hewan_username(self, usernameInput):
        cursor = self.db.cursor()
        sql = """SELECT t.idTransaksi, t.waktuTransaksi, t.usernamePetugas, t.usernamePelanggan, 
                 dt.namaPeliharaan, k.namaKategori, k.biaya,
                 TIMESTAMPDIFF(HOUR, t.waktuTransaksi, NOW())
                 FROM tb_transaksi t join tb_detailtransaksi dt
                 on t.idTransaksi = dt.idTransaksi join tb_kategorihewan k
                 on dt.idKategori = k.idKategori
                 WHERE t.waktuPengembalian is NULL and t.usernamePelanggan = %s
                 ORDER BY t.idTransaksi asc"""
        val = (usernameInput,)
        cursor.execute(sql, val)
        hasil = cursor.fetchall()
        return hasil

    def ambil_username_data_riwayat(self, usernameInput):
        cursor = self.db.cursor()
        sql = """SELECT t.idTransaksi, t.waktuTransaksi, t.waktuPengembalian, t.usernamePetugas, t.usernamePelanggan, 
                 dt.namaPeliharaan, k.namaKategori, k.biaya,
                 TIMESTAMPDIFF(HOUR, t.waktuTransaksi, t.waktuPengembalian)
                 FROM tb_transaksi t join tb_detailtransaksi dt
                 on t.idTransaksi = dt.idTransaksi join tb_kategorihewan k
                 on dt.idKategori = k.idKategori
                 WHERE t.waktuPengembalian is not NULL and t.usernamePelanggan = %s
                 ORDER BY t.idTransaksi asc"""
        val = (usernameInput,)
        cursor.execute(sql, val)
        hasil = cursor.fetchall()
        return hasil



