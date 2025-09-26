Produk = [
    {"nama_produk": "Candra", "harga": "Rp. 300.000.00", "jumlah": "1"},
    {"nama_produk": "Hand-wrap", "harga": "Rp. 78.000.00", "jumlah": "2"},
    {"nama_produk": "Gumshield", "harga": "Rp. 35.000.00", "jumlah": "1"},
]

def Tampilkan_Produk():
    print("\n\tProduk yang tersedia")
    for produk in Produk:
        print(f"Nama : {produk["nama_produk"]}, Harga : {produk["harga"]}, Jumlah : {produk["jumlah"]}")

def Tambahkan_Produk(nama, harga, jumlah):
    Produk.append({"nama_produk": nama, "harga": harga, "jumlah": jumlah})
    print(f"\n{jumlah} produk {nama} dengan harga {harga} berhasil ditambahkan!")

def Menu():
    Tampilkan_Produk()
    Tambahkan_Produk("Glove", "Rp. 100.000.00", "2")
    Tampilkan_Produk()

Menu()