from utils import baca_data, simpan_data
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("=" * 45)
    print("📂  DAFTAR DOKUMEN")
    print("=" * 45)


def lihat_dokumen():
    clear()
    header()

    data = baca_data()

    if not data:
        print("\n⚠️  Tidak ada dokumen.")
        input("\nTekan ENTER untuk kembali...")
        return

    print("\n📄  LIST DOKUMEN (Terbaru di atas)")
    print("-" * 45)

    for i, doc in enumerate(reversed(data), start=1):
        print(f"{i}. 📌 {doc['nama']}")
        print(f"    📁 File    : {doc['file']}")
        print(f"    📅 Tanggal : {doc['tanggal']}")
        print("-" * 45)

    while True:
        hapus = input("\n🗑️  Hapus dokumen? (y/n): ").lower()

        if hapus == 'y':
            try:
                index = int(input("👉 Masukkan nomor dokumen: "))

                if 1 <= index <= len(data):
                    data.pop(len(data) - index)
                    simpan_data(data)

                    print("\n✅ Dokumen berhasil dihapus!")
                else:
                    print("\n❌ Nomor tidak valid!")

            except ValueError:
                print("\n❌ Input harus angka!")

            input("\nTekan ENTER untuk lanjut...")
            break

        elif hapus == 'n':
            print("\n↩️  Kembali ke menu...")
            input("Tekan ENTER...")
            break

        else:
            print("❌ Pilihan hanya y atau n!")