import os
import csv
import json
import logging

# --- Setup logging sederhana ---
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# --- 1) Membuat folder data (jika belum ada) ---
folder = "data"
if not os.path.exists(folder):
    os.makedirs(folder)

# --- 2) Menulis file CSV data/presensi.csv ---
try:
    logging.info("Menulis file CSV presensi...")

    with open(os.path.join(folder, "presensi.csv"), mode="w", newline="") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(["nim", "nama", "hadir_uts"])
        writer.writerow(["23001", "RANGGA", 1])
        writer.writerow(["23002", "VALENT", 0])
        writer.writerow(["23003", "AL NINO", 1])

    logging.info("File CSV berhasil dibuat.")
except Exception as e:
    logging.error(f"Gagal menulis CSV: {e}")

# --- 3) Membaca kembali CSV dan menghitung ringkasan ---
try:
    logging.info("Membaca file CSV dan menghitung ringkasan...")

    with open(os.path.join(folder, "presensi.csv"), mode="r") as file_csv:
        reader = csv.DictReader(file_csv)
        data = list(reader)

        total = len(data)
        hadir = sum(int(row["hadir_uts"]) for row in data)
        persentase = (hadir / total) * 100

    ringkasan = {
        "total_mahasiswa": total,
        "hadir": hadir,
        "persentase_hadir": f"{persentase:.2f}%"
    }

    # Simpan ke JSON
    with open(os.path.join(folder, "ringkasan.json"), mode="w") as file_json:
        json.dump(ringkasan, file_json, indent=4)

    logging.info("Ringkasan berhasil disimpan ke ringkasan.json.")
except Exception as e:
    logging.error(f"Gagal membaca atau menulis file: {e}")