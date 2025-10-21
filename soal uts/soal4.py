def jadwal_hari(hari):
    """
    Menampilkan jadwal kuliah berdasarkan hari.
    """
    jadwal = [
        ["Senin", "Algoritma dan Pemrograman"],
        ["Selasa", "Struktur Data"],
        ["Rabu", "Basis Data"],
        ["Kamis", "Pemrograman Web"],
        ["Jumat", "Jaringan Komputer"]
    ]

    for item in jadwal:
        if item[0].lower() == hari.lower():
            return f"Jadwal hari {hari}: {item[1]}"
    return "Hari tidak ditemukan."


# === Pemanggilan lewat input terminal ===
hari_input = input("Masukkan nama hari: ")
print(jadwal_hari(hari_input))
