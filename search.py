from utils import baca_data
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("=" * 45)
    print("🔍  SEARCH DOKUMEN")
    print("=" * 45)


def search_dokumen():
    clear()
    header()

    data = baca_data()

    if not data:
        print("\n⚠️  Tidak ada data dokumen.")
        input("\nTekan ENTER untuk kembali...")
        return

    keyword = input("\n🔎 Masukkan keyword: ").lower()

    hasil = [
        d for d in data
        if keyword in d['nama'].lower() or keyword in d['file'].lower()
    ]

    print("\n📊 HASIL PENCARIAN")
    print("-" * 45)

    if not hasil:
        print("❌ Tidak ditemukan dokumen yang cocok.")
    else:
        print(f"✅ Ditemukan {len(hasil)} dokumen\n")

        for i, d in enumerate(hasil, 1):
            print(f"{i}. 📌 {d['nama']}")
            print(f"    📁 File    : {d['file']}")
            print(f"    📅 Tanggal : {d['tanggal']}")
            print("-" * 45)

    input("\nTekan ENTER untuk kembali...")