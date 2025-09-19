Keranjang_belanja = [
    {"nama_barang": "Baju", "harga": "Rp. 10.000.00", "jumlah": "1"},
    {"nama_barang": "Celana", "harga": "Rp. 15.000.00", "jumlah": "1"}
]

for data in Keranjang_belanja:
    print(f"Barang : {data['nama_barang']}, Harga : {data['harga']}, Jumlah : {data['jumlah']}")

Keranjang_belanja.append({"nama_barang": "Sepatu", "harga": "Rp. 20.000.00", "jumlah": "2"})

print("\n\tPERUBAHAN")
for data in Keranjang_belanja:
    print(f"Barang : {data['nama_barang']}, Harga : {data['harga']}, Jumlah : {data['jumlah']}")

print("\n\tPANGGILAN KHUSUS")
print(f"Nama barang urutan pertama : {Keranjang_belanja[0]["nama_barang"]}")
print(f"Harga barang urutan kedua : {Keranjang_belanja[1]["harga"]}")