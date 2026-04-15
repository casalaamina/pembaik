from tambah import tambah_dokumen
from lihat import lihat_dokumen
from proses import proses_dokumen
from search import search_dokumen
from sort import sort_dokumen
from utils import baca_riwayat
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("=" * 45)
    print("📂  SISTEM TUMPUKAN DOKUMEN (STACK)")
    print("=" * 45)


def lihat_riwayat():
    clear()
    header()

    data = baca_riwayat()

    if not data:
        print("\n⚠️  Belum ada riwayat.")
    else:
        print("\n📜  RIWAYAT DOKUMEN")
        print("-" * 45)
        for i, d in enumerate(data, 1):
            print(f"{i}. {d}")
        print("-" * 45)

    input("\nTekan ENTER untuk kembali...")


def menu():
    while True:
        clear()
        header()

        print("\n📌  MENU UTAMA")
        print("-" * 45)
        print("1. 📄  Lihat semua dokumen")
        print("2. ➕  Tambah dokumen")
        print("3. ⚙️  Proses dokumen (LIFO)")
        print("4. 🔍  Searching")
        print("5. 📊  Sorting")
        print("6. 📜  Riwayat")
        print("7. ❌  Keluar")
        print("-" * 45)

        pilih = input("👉 Pilih menu (1-7): ")

        if pilih == "1":
            clear()
            header()
            lihat_dokumen()
            input("\nTekan ENTER untuk kembali...")

        elif pilih == "2":
            clear()
            header()
            tambah_dokumen()
            input("\nTekan ENTER untuk kembali...")

        elif pilih == "3":
            clear()
            header()
            proses_dokumen()
            input("\nTekan ENTER untuk kembali...")

        elif pilih == "4":
            clear()
            header()
            search_dokumen()
            input("\nTekan ENTER untuk kembali...")

        elif pilih == "5":
            clear()
            header()
            sort_dokumen()
            input("\nTekan ENTER untuk kembali...")

        elif pilih == "6":
            lihat_riwayat()

        elif pilih == "7":
            clear()
            print("\n👋 Terima kasih sudah menggunakan sistem!")
            break

        else:
            print("\n❌ Pilihan tidak valid!")
            input("Tekan ENTER untuk coba lagi...")


menu()