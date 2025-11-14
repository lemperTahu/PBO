import json
class Pegawai:
    def __init__(self, id_pegawai, nama, jabatan, gaji):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

class Kepegawaian:
    def __init__(self):
        self.daftar_pegawai = []

    def tambah_pegawai(self, id_pegawai, nama, jabatan, gaji):
        self.daftar_pegawai.append(Pegawai(id_pegawai, nama, jabatan, gaji))
        print(f"✅ Pegawai {nama} berhasil ditambahkan.")

    def total_gaji(self):
        return sum(p.gaji for p in self.daftar_pegawai)

    def simpan_data(self):
        data = [{"id_pegawai": p.id_pegawai, "nama": p.nama, "jabatan": p.jabatan, "gaji": p.gaji}
                for p in self.daftar_pegawai]
        with open("data_pegawai.json", "w") as f:
            json.dump(data, f, indent=4)
