import json
from datetime import datetime
from inventory import Inventori

class Penjualan:
    def __init__(self):
        self.transaksi = []

    def tambah_transaksi(self, nama_produk, jumlah, inventori):
        produk = inventori.cari_produk(nama_produk)
        if produk and jumlah <= produk.stok:
            total = produk.harga_jual * jumlah
            produk.update_stok(jumlah)
            self.transaksi.append({
                "produk": nama_produk,
                "jumlah": jumlah,
                "total": total,
                "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            print(f"✅ Transaksi berhasil: {nama_produk} x{jumlah} = Rp{total:,}")
        else:
            print("⚠️ Produk tidak ditemukan atau stok kurang.")

    def simpan_penjualan(self):
        with open("data_penjualan.json", "w") as f:
            json.dump(self.transaksi, f, indent=4)
