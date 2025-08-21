class Buku:
    def __init__(self, isbn, judul, pengarang, jumlah, terpinjam=0):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = terpinjam

    def __str__(self):
        return f"ISBN: {self.isbn} - Judul: {self.judul} - Pengarang: {self.pengarang} - Jumlah: {self.jumlah} - Terpinjam: {self.terpinjam}"

books = [
    Buku("9786237121144", "Kumpulan Solusi Pemrograman Python", "Budi Raharjo", 6, 0),
    Buku("9786231800718", "Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "Okta Purnawirawan", 15, 0),
    Buku("9786026163905", "Analisis dan Perancangan Sistem Informasi", "Adi Sulistyo Nugroho", 2, 1),
    Buku("9786022912828", "Animal Farm", "George Orwell", 4, 0)
]

records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]


def tampilkan_data():
    print("\n== Daftar Buku ==")
    for i, buku in enumerate(books, start=1):
        print(f"{i}. {buku}")


def tambah_data():
    isbn = input("Masukkan no ISBN: ")
    judul = input("Masukkan Judul Buku: ")
    pengarang = input("Masukkan nama pengarang: ")
    jumlah = int(input("Masukkan jumlah buku: "))
    terpinjam = int(input("Masukkan jumlah yang terpinjam: "))
    buku_baru = Buku(isbn, judul, pengarang, jumlah, terpinjam)
    books.append(buku_baru)
    print("Buku berhasil ditambahkan!\n")

def edit_data():
    tampilkan_data()
    indeks_ubah = int(input("Masukkan nomor data yang ingin diubah: ")) - 1
    if 0 <= indeks_ubah < len(books):
        isbn = input("Masukkan no ISBN baru: ")
        judul = input("Masukkan judul buku baru: ")
        pengarang = input("Masukkan nama pengarang baru: ")
        jumlah = int(input("Masukkan jumlah buku baru: "))
        terpinjam = int(input("Masukkan jumlah terpinjam baru: "))
        
        books[indeks_ubah].isbn = isbn
        books[indeks_ubah].judul = judul
        books[indeks_ubah].pengarang = pengarang
        books[indeks_ubah].jumlah = jumlah
        books[indeks_ubah].terpinjam = terpinjam
        
        print("Data berhasil diubah!")
    else:
        print("Nomor data tidak valid!")


def hapus_data():
    tampilkan_data()
    indeks_hapus = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
    if 0 <= indeks_hapus < len(books):
        del books[indeks_hapus]
        print("Data berhasil dihapus!")
    else:
        print("Nomor data tidak valid!")
    menu()

def tampilkan_peminjaman():
    print("\n== Data Peminjaman ==")
    for i, record in enumerate(records, start=1):
        print(f"{i}. ISBN: {record['isbn']} - Status: {record['status']} - Pinjam: {record['tanggal_pinjam']} - Kembali: {record['tanggal_kembali']}")

def tampilkan_belum():
    print("\n== Peminjaman Belum Kembali ==")
    found = False
    for record in records:
        if record['status'] == "Belum":
            print(f"ISBN: {record['isbn']} - Tanggal Pinjam: {record['tanggal_pinjam']} - Tanggal Kembali: {record['tanggal_kembali']}")
            found = True
    if not found:
        print("Tidak ada buku yang belum kembali.")

def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    for buku in books:
        if buku.isbn == isbn:
            if buku.jumlah > buku.terpinjam:
                buku.terpinjam += 1
                records.append({"isbn": isbn, "status": "Belum", "tanggal_pinjam": "2025-03-21", "tanggal_kembali": ""})
                print("Buku berhasil dipinjam.")
            else:
                print("Buku sudah habis dipinjam.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")

def pengembalian():
    isbn = input("Masukkan ISBN buku yang ingin dikembalikan: ")
    balik_buku = input("Tanggal buku dikembalikan (YYYY-MM-DD): ")
    for buku in books:
        if buku.isbn == isbn:
            if buku.terpinjam > 0:
                buku.terpinjam -= 1
                for record in records:
                    if record['isbn'] == isbn and record['status'] == "Belum":
                        record['status'] = "Selesai"
                        record['tanggal_kembali'] = balik_buku
                        break
                print("Buku berhasil dikembalikan.")
            else:
                print("Buku ini tidak sedang dipinjam.")
            return
    print("Buku dengan ISBN ini tidak ditemukan.")


def menu():
    while True:
        print("\n---=== MENU ===---")
        print("[1] Tampilkan Data")
        print("[2] Tambah Data")
        print("[3] Edit Data")
        print("[4] Hapus Data")
        print("[5] Tampilkan Semua Peminjaman")
        print("[6] Tampilkan Peminjaman Belum Kembali")
        print("[7] Peminjaman")
        print("[8] Pengembalian")
        print("[X] Keluar")

        pilihan = input("Masukkan pilihan menu (1-8 atau X): ")
        
        match pilihan:
            case "1":
                tampilkan_data()
            case "2":
                tambah_data()
            case "3":
                edit_data()
            case "4":
                hapus_data()
            case "5":
                tampilkan_peminjaman()
            case "6":
                tampilkan_belum()
            case "7":
                peminjaman()
            case "8":
                pengembalian()
            case "x" | "X":
                print("Keluar dari program")
                break
            case _:
                print("Pilihan tidak valid!")

menu()
