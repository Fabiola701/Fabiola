# listfunctions.py

print(" FUNGSI-FUNGSI LIST ")

# 1. Inisialisasi List
mylist = [10, 20, 30, 40, 50]
print(f"\nList Awal: {mylist}")

# 2. append(): Menambahkan elemen ke akhir list
mylist.append(60)
print(f"Setelah append(60): {mylist}")

# 3. extend(): Menambahkan elemen dari iterable lain ke akhir list
another_list = [70, 80]
mylist.extend(another_list)
print(f"Setelah extend([70, 80]): {mylist}")

# 4. insert(): Menambahkan elemen pada indeks tertentu
mylist.insert(0, 5) # Menambahkan 5 di indeks 0
print(f"Setelah insert(0, 5): {mylist}")

# 5. remove(): Menghapus elemen pertama yang cocok
mylist.remove(20) # Menghapus elemen 20
print(f"Setelah remove(20): {mylist}")

# 6. pop(): Menghapus dan mengembalikan elemen pada indeks tertentu (default: terakhir)
popped_element = mylist.pop() # Menghapus elemen terakhir
print(f"Setelah pop() (elemen terakhir): {mylist}")
print(f"Elemen yang di-pop: {popped_element}")

popped_element_at_index = mylist.pop(1) # Menghapus elemen di indeks 1 (sekarang 10)
print(f"Setelah pop(1) (elemen di indeks 1): {mylist}")
print(f"Elemen yang di-pop dari indeks 1: {popped_element_at_index}")

# 7. clear(): Menghapus semua elemen dari list
temp_list = [1, 2, 3]
print(f"List temporer sebelum clear(): {temp_list}")
temp_list.clear()
print(f"Setelah clear(): {temp_list}")

# 8. index(): Mengembalikan indeks dari elemen pertama yang cocok
index_of_30 = mylist.index(30)
print(f"Indeks dari 30: {index_of_30}")

# 9. count(): Mengembalikan jumlah kemunculan elemen
list_with_duplicates = [1, 2, 2, 3, 2, 4]
count_of_2 = list_with_duplicates.count(2)
print(f"List dengan duplikat: {list_with_duplicates}")
print(f"Jumlah kemunculan 2: {count_of_2}")

# 10. sort(): Mengurutkan elemen-elemen dalam list (in-place)
unsorted_list = [5, 2, 8, 1, 9]
print(f"List belum diurutkan: {unsorted_list}")
unsorted_list.sort()
print(f"Setelah sort() (ascending): {unsorted_list}")

unsorted_list.sort(reverse=True) # Mengurutkan secara descending
print(f"Setelah sort(reverse=True) (descending): {unsorted_list}")

# 11. reverse(): Membalik urutan elemen dalam list (in-place)
original_order_list = [1, 2, 3, 4, 5]
print(f"List urutan asli: {original_order_list}")
original_order_list.reverse()
print(f"Setelah reverse(): {original_order_list}")

# 12. copy(): Membuat salinan dangkal (shallow copy) dari list
original_list = [10, 20, 30]
copied_list = original_list.copy()
print(f"List asli: {original_list}")
print(f"List hasil copy: {copied_list}")

# Mengubah list yang dicopy tidak akan mempengaruhi list asli (untuk shallow copy)
copied_list.append(40)
print(f"List asli setelah copy diubah: {original_list}")
print(f"List hasil copy setelah diubah: {copied_list}")

print("\n SELESAI ")