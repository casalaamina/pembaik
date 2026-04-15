import datetime
import os
import shutil
from utils import baca_data, simpan_data
from tkinter import Tk, filedialog


def pilih_file():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Pilih Dokumen",
        filetypes=[
            ("PDF files", "*.pdf"),
            ("Word files", "*.docx")
        ]
    )

    return file_path


def tambah_dokumen():
    data = baca_data()

    nama = input("Nama dokumen: ")

    print("Pilih file dokumen...")
    file_path = pilih_file()

    if not file_path:
        print("Tidak ada file dipilih.")
        return

    if not (file_path.endswith(".pdf") or file_path.endswith(".docx")):
        print("Format harus PDF/DOCX!")
        return

    # 🔥 Ambil nama file saja
    nama_file = os.path.basename(file_path)

    # 🔥 Buat folder jika belum ada
    folder_tujuan = "file_dokumen"
    if not os.path.exists(folder_tujuan):
        os.makedirs(folder_tujuan)

    # 🔥 Path tujuan
    tujuan = os.path.join(folder_tujuan, nama_file)

    # 🔥 Copy file ke folder project
    shutil.copy(file_path, tujuan)

    tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data.append({
        "nama": nama,
        "file": nama_file,
        "tanggal": tanggal
    })

    simpan_data(data)
    print("Dokumen berhasil ditambahkan & disimpan ke folder!")