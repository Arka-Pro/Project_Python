print("==[Perhitungan rumus pythagoras]==")
a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))
c = int(input("Masukkan nilai c : "))

def pythagoras():
    perhitungan  = a*2 + b*2 + c*2
    hasil = perhitungan
    return hasil

print(f"Hasilnya adalah : {pythagoras()}")