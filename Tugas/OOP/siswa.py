class Siswa:
    def __init__(self, nama, umur, kelas, absensi):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas
        self.absensi = absensi

    def function(self):
        print("Nulis")
        
Narsul = Siswa("Narsul", 16, "X", 30)
print(Narsul.nama)
print(Narsul.umur)
print(Narsul.kelas)
print(Narsul.absensi)
Narsul.function()