# Deklarasi metriks pertama dan kedua
metriks1 = []
metriks2 = []

# Meminta input untuk metriks pertama
print("Memasukkan elemen untuk metriks pertama:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))#
        baris.append(nilai)
    metriks1.append(baris)
    
# Meminta input untuk metriks kedua
print("\nMasukkan elemen untuk metriks kedua:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    metriks2.append(baris)
    
# Penjulahan metriks
hasil = []
for i in range(2):
    baris = []
    for j in range(2):
        baris.append(metriks1[i][j] + metriks2[i][j])
    hasil.append(baris)
    
# Menampilkkan hasil penjumlahan
print("\nHasil penjumlahan metriks:")
for baris in hasil:
    print(baris)