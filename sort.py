from utils import baca_data
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("=" * 45)
    print("📊  SORTING DOKUMEN")
    print("=" * 45)


def sort_dokumen():
    clear()
    header()

    data = baca_data()

    if not data:
        print("\n⚠️  Tidak ada data dokumen.")
        input("\nTekan ENTER untuk kembali...")
        return

    print("\n📌 Pilih metode sorting:")
    print("-" * 45)
    print("1. 🔤 Nama (A-Z)")
    print("2. 📅 Tanggal (Terlama → Terbaru)")
    print("-" * 45)

    pilihan = input("👉 Pilih (1/2): ")

    if pilihan == "1":
        hasil = sorted(data, key=lambda x: x['nama'].lower())
        metode = "Nama (A-Z)"

    elif pilihan == "2":
        hasil = sorted(data, key=lambda x: x['tanggal'])
        metode = "Tanggal (Terlama → Terbaru)"

    else:
        print("\n❌ Pilihan tidak valid!")
        input("Tekan ENTER untuk kembali...")
        return

    print(f"\n📊 Hasil Sorting: {metode}")
    print("-" * 45)

    for i, d in enumerate(hasil, 1):
        print(f"{i}. 📌 {d['nama']}")
        print(f"    📁 File    : {d['file']}")
        print(f"    📅 Tanggal : {d['tanggal']}")
        print("-" * 45)

    input("\nTekan ENTER untuk kembali...")