from utils import baca_data, simpan_data, tambah_riwayat
import os
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("=" * 45)
    print("⚙️  PROSES DOKUMEN (LIFO)")
    print("=" * 45)


def proses_dokumen():
    clear()
    header()

    data = baca_data()

    if not data:
        print("\n⚠️  Tidak ada dokumen untuk diproses.")
        input("\nTekan ENTER untuk kembali...")
        return

    print("\n📦 Mengambil dokumen paling atas...")
    print("-" * 45)

    # animasi sederhana
    print("⏳ Memproses", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print()

    dokumen = data.pop()  # LIFO
    simpan_data(data)
    tambah_riwayat(dokumen)

    print("\n✅ Dokumen berhasil diproses!")
    print("-" * 45)
    print(f"📌 Nama    : {dokumen['nama']}")
    print(f"📁 File    : {dokumen['file']}")
    print(f"📅 Tanggal : {dokumen['tanggal']}")
    print("-" * 45)

    print("\n📜 Dokumen telah dipindahkan ke riwayat.")
    input("\nTekan ENTER untuk kembali...")