class Mahasiswa23:
    def __init__(self, nama, nim, kelas):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.nilai = -1

    def tugasDinilai(self, nilai):
        self.nilai = nilai