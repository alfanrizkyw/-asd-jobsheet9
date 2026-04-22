from Mahasiswa23 import Mahasiswa23

class StackTugasMahasiswa23:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def isFull(self):
        return self.top == self.size - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, mhs):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = mhs
        else:
            print("Stack penuh! Tidak bisa menambah tugas lagi.")

    def pop(self):
        if not self.isEmpty():
            m = self.stack[self.top]
            self.top -= 1
            return m
        else:
            print("Stack kosong! Tidak ada tugas untuk dinilai")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            print("Stack kosong! Tidak ada tugas yang dikumpulkan")
            return None

    def print_stack(self):
        if not self.isEmpty():
            # Range top + 1 agar elemen terakhir ikut ter-print
            for i in range(self.top + 1):
                m = self.stack[i]
                print(f"{m.nama}\t{m.nim}\t{m.kelas}")
            print("")