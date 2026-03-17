import datetime
import statistics

def main():
    #Struktur Data
    data_kelas = {
        "Dzikru": 85,
        "Yunus": 60,
        "Habibi": 92,
        "Dammar": 78,
        "Serena": 80
    }

    print("Laporan Hasil Ujian Tengah Semester Mahasiswa")
    waktu_sekarang = datetime.datetime.now().strftime("%d %B %Y")
    print(f"Tanggal Laporan: {waktu_sekarang}\n")
    kumpulan_nilai = list(data_kelas.values())
    rata_rata = statistics.mean(kumpulan_nilai)
    print(f"Rata-rata Nilai Kelas: {rata_rata}\n")
    print("Rincian Kelulusan Mahasiswa:")
    
    #Struktur Kontrol
    for nama, nilai in data_kelas.items():
        if nilai >= 70:
            keterangan = "LULUS"
        else:
            keterangan = "REMEDIAL"
        print(f"{nama}: {nilai} (Keterangan: {keterangan})")
if __name__ == "__main__":
    main()