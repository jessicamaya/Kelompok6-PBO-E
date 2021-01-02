class TryCatcher():
    def __init__(self):
        self.listKondisiInt = ["Masukkan menu yang dipilih : "]
        self.listKondisiStr = ["Masukkan username : ", "Masukkan password : "]

    def check_int(self, param1 = None, param2 = None, menu = None):
        if menu == None:
            menu = self.listKondisiInt[0]
        while True:
            try:
                inputan = int(input(menu))
                if param1 != None and param2 != None:
                    if inputan < param1 or inputan > param2:
                        raise ValueError
                break
            except ValueError:
                pesan = "Angka tidak valid. Masukkan lagi."
                print(pesan)
        return inputan

    def check_str(self, menu):
        while True:
            try:
                inputan = str(input(menu))
                float(inputan)/0
            except ZeroDivisionError:
                print("Masukan yang diperbolehkan hanya berupa kata-kata, atau alphanumeric.")
            except ValueError:
                break
        return inputan      
        
