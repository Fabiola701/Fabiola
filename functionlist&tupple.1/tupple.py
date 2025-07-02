# tuplefunctions.py

print("FUNGSI-FUNGSI TUPLE")

# 1. Tuple
mytuple = (10, 20, 30, 40, 50)
print(f"\nTuple Awal: {mytuple}")

# Tuple adalah immutable, artinya elemennya tidak bisa diubah, ditambah, atau dihapus
# Jadi, tidak ada fungsi seperti append(), extend(), insert(), remove(), pop(), clear(), sort(), reverse()

# 2. count(): Mengembalikan jumlah kemunculan elemen
tuple_with_duplicates = (1, 2, 2, 3, 2, 4)
count_of_2 = tuple_with_duplicates.count(2)
print(f"Tuple dengan duplikat: {tuple_with_duplicates}")
print(f"Jumlah kemunculan 2: {count_of_2}")

# 3. index(): Mengembalikan indeks dari elemen pertama yang cocok
index_of_30 = mytuple.index(30)
print(f"Indeks dari 30: {index_of_30}")

# Fungsi built-in Python yang bekerja dengan tuple:
# 4. len(): Mengembalikan jumlah elemen dalam tuple
print(f"Panjang tuple (len(my_tuple)): {len(mytuple)}")

# 5. max(): Mengembalikan elemen terbesar dalam tuple
print(f"Elemen terbesar (max(my_tuple)): {max(mytuple)}")

# 6. min(): Mengembalikan elemen terkecil dalam tuple
print(f"Elemen terkecil (min(my_tuple)): {min(mytuple)}")

# 7. sum(): Mengembalikan jumlah semua elemen numerik dalam tuple
print(f"Jumlah semua elemen (sum(my_tuple)): {sum(mytuple)}")

# 8. tuple(): Mengkonversi iterable lain ke tuple
list_to_convert = [1, 2, 3]
converted_tuple = tuple(list_to_convert)
print(f"List yang dikonversi ke tuple: {converted_tuple}")

print("\n SELESAI ")