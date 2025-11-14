import json
import os

class Produk:
    def __init__(self, id_produk, nama, harga_beli, harga_jual, stok):
        self.id_produk = id_produk
        self.nama = nama
        self.harga_beli = harga_beli
        self.harga_jual = harga_jual
        self.stok = stok

    def update_stok(self, jumlah_terjual):
        if jumlah_terjual <= self.stok:
            self.stok -= jumlah_terjual
        else:
            print(f"⚠️ Stok tidak cukup untuk {self.nama}.")

class Material(Produk):
    def __init__(self, id_produk, nama, harga_beli, harga_jual, stok, jenis_bahan):
        super().__init__(id_produk, nama, harga_beli, harga_jual, stok)
        self.jenis_bahan = jenis_bahan

class Perlengkapan(Produk):
    def __init__(self, id_produk, nama, harga_beli, harga_jual, stok, merek):
        super().__init__(id_produk, nama, harga_beli, harga_jual, stok)
        self.merek = merek

class Kategori:
    def __init__(self, nama_kategori):
        self.nama_kategori = nama_kategori
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

class Inventori:
    def __init__(self):
        self.daftar_kategori = [
            Kategori("Material"),
            Kategori("Perlengkapan")
        ]

    def cari_kategori(self, nama_kategori):
        for kategori in self.daftar_kategori:
            if kategori.nama_kategori.lower() == nama_kategori.lower():
                return kategori
        return None

    def cari_produk(self, nama_produk):
        for kategori in self.daftar_kategori:
            for produk in kategori.daftar_produk:
                if produk.nama.lower() == nama_produk.lower():
                    return produk
        return None

    def tampilkan_semua(self):
        for kategori in self.daftar_kategori:
            print(f"\nKategori: {kategori.nama_kategori}")
            if not kategori.daftar_produk:
                print("   (Belum ada produk)")
            for p in kategori.daftar_produk:
                print(f"- {p.nama} | Stok: {p.stok}")

    def tambah_produk_input(self):
        print("\n=== TAMBAH PRODUK BARU ===")
        print("Pilih kategori:")
        print("1. Material")
        print("2. Perlengkapan")

        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == "1":
            kategori = self.cari_kategori("Material")
        elif pilihan == "2":
            kategori = self.cari_kategori("Perlengkapan")
        else:
            print("Pilihan tidak valid.")
            return

        id_produk = input("Masukkan ID produk: ")
        nama = input("Masukkan nama produk: ")
        harga_beli = int(input("Masukkan harga beli: "))
        harga_jual = int(input("Masukkan harga jual: "))
        stok = int(input("Masukkan jumlah stok: "))

        if kategori.nama_kategori == "Material":
            jenis_bahan = input("Masukkan jenis bahan (contoh: semen, kayu, besi): ")
            produk_baru = Material(id_produk, nama, harga_beli, harga_jual, stok, jenis_bahan)
        else:
            merek = input("Masukkan merek perlengkapan: ")
            produk_baru = Perlengkapan(id_produk, nama, harga_beli, harga_jual, stok, merek)

        kategori.tambah_produk(produk_baru)
        self.simpan_inventori()
        print(f"✅ Produk '{nama}' berhasil ditambahkan ke kategori '{kategori.nama_kategori}'.")

    # 🧩 Pindahkan fungsi simpan ke dalam class
    def simpan_inventori(self):
        data = []
        for kategori in self.daftar_kategori:
            data.append({
                "nama_kategori": kategori.nama_kategori,
                "produk": [{
                    "id_produk": p.id_produk,
                    "nama": p.nama,
                    "harga_beli": p.harga_beli,
                    "harga_jual": p.harga_jual,
                    "stok": p.stok,
                    "jenis": "material" if isinstance(p, Material) else "perlengkapan"
                } for p in kategori.daftar_produk]
            })
        with open("data_inventori.json", "w") as f:
            json.dump(data, f, indent=4)
        print("💾 Data inventori berhasil disimpan ke 'data_inventori.json'.")
