import json
import os
class Accounting:
    def __init__(self):
        self.pemasukan = 0
        self.pengeluaran = 0

    def hitung_pemasukan(self):
        if not os.path.exists("data_penjualan.json"):
            return 0
        with open("data_penjualan.json", "r") as f:
            data = json.load(f)
        self.pemasukan = sum(t["total"] for t in data)
        return self.pemasukan

    def hitung_pengeluaran(self):
        if not os.path.exists("data_pegawai.json"):
            return 0
        with open("data_pegawai.json", "r") as f:
            pegawai = json.load(f)
        self.pengeluaran = sum(p["gaji"] for p in pegawai)
        return self.pengeluaran

    def laporan_keuangan(self):
        laba_bersih = self.hitung_pemasukan() - self.hitung_pengeluaran()
        print("\n=== LAPORAN KEUANGAN TOKO ===")
        print(f"Total Pemasukan : Rp{self.pemasukan:,}")
        print(f"Total Pengeluaran: Rp{self.pengeluaran:,}")
        print(f"💰 Laba Bersih  : Rp{laba_bersih:,}")
