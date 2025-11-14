# ==============================
# SISTEM MANAJEMEN TOKO BANGUNAN (LOGIN + MENU UTAMA)
# ==============================

from inventory import Inventori
from penjualan import Penjualan
from kepegawaian import Kepegawaian
from accounting import Accounting

# === DATA LOGIN SEDERHANA ===
AKUN = {
    "admin": {"password": "admin123", "role": "admin"},
    "kasir": {"password": "kasir123", "role": "kasir"}
}


# ==============================
# FUNGSI LOGIN
# ==============================
def login():
    print("=== LOGIN SISTEM TOKO BANGUNAN ===")
    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in AKUN and AKUN[username]["password"] == password:
            print(f"\n✅ Login berhasil sebagai {AKUN[username]['role'].upper()}")
            return AKUN[username]["role"]
        else:
            print("❌ Username atau password salah. Coba lagi.\n")


# ==============================
# MENU ADMIN
# ==============================
def menu_admin(inventori, penjualan, kepegawaian, accounting):
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat Produk & Stok")
        print("2. Tambah Produk Baru")
        print("3. Catat Penjualan")
        print("4. Data Kepegawaian")
        print("5. Laporan Accounting")
        print("6. Keluar")

        pilih = input("Pilih menu (1-6): ")

        if pilih == "1":
            inventori.tampilkan_semua()

        elif pilih == "2":
            inventori.tambah_produk_input()

        elif pilih == "3":
            nama_produk = input("Masukkan nama produk: ")
            jumlah = int(input("Jumlah terjual: "))
            penjualan.tambah_transaksi(nama_produk, jumlah, inventori)
            penjualan.simpan_penjualan()

        elif pilih == "4":
            nama = input("Nama pegawai: ")
            jabatan = input("Jabatan: ")
            gaji = int(input("Gaji: "))
            kepegawaian.tambah_pegawai(len(kepegawaian.daftar_pegawai) + 1, nama, jabatan, gaji)
            kepegawaian.simpan_data()

        elif pilih == "5":
            accounting.laporan_keuangan()

        elif pilih == "6":
            print("Keluar dari menu admin.")
            break

        else:
            print("Pilihan tidak valid.")


# ==============================
# MENU KASIR
# ==============================
def menu_kasir(penjualan, inventori):
    while True:
        print("\n=== MENU KASIR ===")
        print("1. Catat Penjualan")
        print("2. Lihat Stok Barang")
        print("3. Keluar")

        pilih = input("Pilih menu (1-3): ")

        if pilih == "1":
            nama_produk = input("Masukkan nama produk: ")
            jumlah = int(input("Jumlah terjual: "))
            penjualan.tambah_transaksi(nama_produk, jumlah, inventori)
            penjualan.simpan_penjualan()
        elif pilih == "2":
            inventori.tampilkan_semua()
        elif pilih == "3":
            print("Keluar dari menu kasir.")
            break
        else:
            print("Pilihan tidak valid.")


# ==============================
# PROGRAM UTAMA
# ==============================
def main():
    inventori = Inventori()
    penjualan = Penjualan()
    kepegawaian = Kepegawaian()
    accounting = Accounting()

    # Jalankan login dulu
    role = login()

    # Arahkan ke menu sesuai role
    if role == "admin":
        menu_admin(inventori, penjualan, kepegawaian, accounting)
    elif role == "kasir":
        menu_kasir(penjualan, inventori)
    else:
        print("Peran tidak dikenali.")

    print("\nProgram selesai ✅")


# Jalankan program
if __name__ == "__main__":
    main()
