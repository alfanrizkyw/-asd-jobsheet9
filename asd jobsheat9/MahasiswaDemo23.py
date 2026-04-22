from Mahasiswa23 import Mahasiswa23
from StackTugasMahasiswa23 import StackTugasMahasiswa23

def main():
    # Inisialisasi stack dengan kapasitas 5
    stack = StackTugasMahasiswa23(5)
    
    pilih = 0
    while True:
        print("\nMenu")
        print("1. Mengumpulkan Tugas")
        print("2. Menilai Tugas")
        print("3. Melihat Tugas Teratas")
        print("4. Melihat Daftar Tugas")
        print("5. Keluar")
        
        try:
            inp = input("Pilih: ")
            if not inp: continue
            pilih = int(inp)
        except ValueError:
            print("Pilihan tidak valid. Masukkan angka.")
            continue

        if pilih == 1:
            nama = input("Nama: ")
            nim = input("NIM: ")
            kelas = input("Kelas: ")
            mhs = Mahasiswa23(nama, nim, kelas)
            stack.push(mhs)
            print(f"Tugas {mhs.nama} berhasil dikumpulkan")

        elif pilih == 2:
            dinilai = stack.pop()
            if dinilai:
                print(f"Menilai tugas dari {dinilai.nama}")
                try:
                    nilai = int(input("Masukkan nilai (0-100): "))
                    dinilai.tugasDinilai(nilai)
                    print(f"Nilai Tugas {dinilai.nama} adalah {nilai}")
                except ValueError:
                    print("Nilai harus berupa angka.")

        elif pilih == 3:
            lihat = stack.peek()
            if lihat:
                print(f"Tugas terakhir dikumpulkan oleh {lihat.nama}")

        elif pilih == 4:
            print("Daftar semua tugas")
            print("Nama\tNIM\tKelas")
            stack.print_stack()

        elif pilih == 5:
            print("\nBerhasil Keluar\n")
            break
            
        else:
            print("Pilihan tidak valid.")
        
        # Kondisi loop agar mirip do-while Java: berhenti jika diluar 1-4
        if pilih < 1 or pilih > 4:
            break

if __name__ == "__main__":
    main()