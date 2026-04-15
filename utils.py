import os

DATA_FILE = "data.txt"
RIWAYAT_FILE = "riwayat.txt"


def baca_data():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        lines = file.readlines()

    data = []
    for line in lines:
        nama, file_doc, tanggal = line.strip().split("|")
        data.append({
            "nama": nama,
            "file": file_doc,
            "tanggal": tanggal
        })
    return data


def simpan_data(data):
    with open(DATA_FILE, "w") as file:
        for d in data:
            file.write(f"{d['nama']}|{d['file']}|{d['tanggal']}\n")


def tambah_riwayat(dokumen):
    with open(RIWAYAT_FILE, "a") as file:
        file.write(f"{dokumen['nama']}|{dokumen['file']}|{dokumen['tanggal']}\n")


def baca_riwayat():
    if not os.path.exists(RIWAYAT_FILE):
        return []

    with open(RIWAYAT_FILE, "r") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]