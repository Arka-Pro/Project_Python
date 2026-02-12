class buah:
    def __init__(self, warna, harga,rasa):
        self.warna = warna
        self.harga = harga
        self.rasa = rasa
    
    def function(self):
        print("nyam nyam nyam")
        
pisang = buah("kuning", 5000, "manis")
print(pisang.warna)
print(pisang.harga)
print(pisang.rasa)
pisang.function()
