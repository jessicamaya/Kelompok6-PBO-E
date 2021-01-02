import eq_database

class LoginModel():
    def __init__(self):
        self.database_var = eq_database.Helper_Database()
        self.database_var.buatDatabase()
        self.database_var.buatTabel()

    def verifikasi_akun(self, loginSebagai, usernameLogin, __passwordLogin):
        hasil = self.database_var.verifikasi_akun(loginSebagai, usernameLogin, __passwordLogin)
        return hasil

    