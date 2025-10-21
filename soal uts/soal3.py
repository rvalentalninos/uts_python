def hitung_ongkir(berat_kg, kota, asuransi=False):
    """Menghitung ongkir RapidSend berdasarkan berat, kota, dan asuransi."""
    tarif_dasar = {
        "Jakarta": 11000,
        "Bandung": 13000,
        "Surabaya": 16000
    }
    ongkir = tarif_dasar.get(kota, 0) + 2000 * berat_kg
    if asuransi:
        ongkir += 3000
    return ongkir

# Contoh pemanggilan:
print(hitung_ongkir(2, "Jakarta"))           # Tanpa asuransi
print(hitung_ongkir(3, "Bandung", True))     # Dengan asuransi