# input() untuk terima data dari user melalui input terminal
# tipe data float() untuk mengubah teks menjadi bilangan pecahan biar bisa dihitung
s1 = float(input("Masukkan setoran minggu 1: "))
s2 = float(input("Masukkan setoran minggu 2: "))
s3 = float(input("Masukkan setoran minggu 3: "))

# validasi input cek apa ada salah satu nilai yang <= 0
# "or" berarti cukup satu pernyataan yang memenuhi kondisi3 maka seluruh pernyataan dianggap sah
if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("Input tidak valid.")
else:
    # hitung total
    # f"...." merupakan cara di python untuk menyisipkan variabel dalam teks
    total = s1 + s2 + s3
    print(f"Total setoran: Rp{total:,.0f}")

    #  Klasifikasi total
    if total <= 300000:
        print("Kategori: rendah")
    elif total <= 600000:  
        print("Kategori: sedang")
    elif total > 600000:
        print("Kategori: tinggi")