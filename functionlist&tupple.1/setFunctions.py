# setFunctions.py

print("Fungsi Bawaan (Built-in Functions) untuk Set di Python")
print("Set adalah koleksi data yang tidak berurutan, tidak dapat diubah (immutable), dan setiap elemennya unik (tidak ada duplikasi).\n")

# --- 1. len() ---
print("--- 1. len() ---")
print("Fungsi len() digunakan untuk mendapatkan jumlah elemen dalam sebuah set.")
my_set = {1, 2, 3, 4, 5}
jumlah_elemen = len(my_set)
print(f"Set: {my_set}")
print(f"Jumlah elemen dalam set: {jumlah_elemen}")

another_set = {'apple', 'banana', 'cherry'}
print(f"Set: {another_set}")
print(f"Jumlah elemen dalam set: {len(another_set)}\n")

# --- 2. min() ---
print("--- 2. min() ---")
print("Fungsi min() digunakan untuk menemukan elemen terkecil dalam sebuah set.")
#Perlu diingat, semua elemen dalam set harus bertipe data yang sama dan dapat dibandingkan.
angka_set = {10, 5, 20, 2, 15}
terkecil = min(angka_set)
print(f"Set: {angka_set}")
print(f"Elemen terkecil: {terkecil}")

huruf_set = {'c', 'a', 'b', 'd'}
terkecil_huruf = min(huruf_set)
print(f"Set: {huruf_set}")
print(f"Elemen terkecil: {terkecil_huruf}\n")

# --- 3. max() ---
print("--- 3. max() ---")
print("Fungsi max() digunakan untuk menemukan elemen terbesar dalam sebuah set.")
#Sama seperti min(), semua elemen harus bertipe data yang sama dan dapat dibandingkan.
angka_set = {10, 5, 20, 2, 15}
terbesar = max(angka_set)
print(f"Set: {angka_set}")
print(f"Elemen terbesar: {terbesar}")

huruf_set = {'c', 'a', 'b', 'd'}
terbesar_huruf = max(huruf_set)
print(f"Set: {huruf_set}")
print(f"Elemen terbesar: {terbesar_huruf}\n")

# --- 4. sum() ---
print("--- 4. sum() ---")
print("Fungsi sum() digunakan untuk menghitung total jumlah (sum) dari semua elemen dalam sebuah set.")
#Fungsi ini hanya bisa digunakan jika semua elemen dalam set bertipe numerik.
angka_set = {1, 2, 3, 4, 5}
total = sum(angka_set)
print(f"Set: {angka_set}")
print(f"Total jumlah elemen: {total}")

nilai_set = {10.5, 20.0, 5.5}
total_nilai = sum(nilai_set)
print(f"Set: {nilai_set}")
print(f"Total jumlah elemen: {total_nilai}\n")

# --- 5. all() ---
print("--- 5. all() ---")
print("Fungsi all() akan mengembalikan True jika semua elemen dalam set bernilai benar (True) atau jika set kosong.")
set_true = {1, True, 'hello'}
print(f"Set: {set_true}")
print(f"Apakah semua elemen True? {all(set_true)}")

set_false = {1, 0, 'hello'} # 0 adalah False
print(f"Set: {set_false}")
print(f"Apakah semua elemen True? {all(set_false)}")

set_kosong = set()
print(f"Set: {set_kosong}")
print(f"Apakah semua elemen True? (set kosong) {all(set_kosong)}\n")

# --- 6. any() ---
print("--- 6. any() ---")
print("Fungsi any() akan mengembalikan True jika setidaknya ada satu elemen dalam set yang bernilai benar (True).")
#Jika semua elemen bernilai salah (False) atau jika set kosong, maka akan mengembalikan False.
set_ada_true = {0, False, 1} # Ada 1 (True)
print(f"Set: {set_ada_true}")
print(f"Apakah ada elemen True? {any(set_ada_true)}")

set_semua_false = {0, False, None}
print(f"Set: {set_semua_false}")
print(f"Apakah ada elemen True? {any(set_semua_false)}")

set_kosong = set()
print(f"Set: {set_kosong}")
print(f"Apakah ada elemen True? (set kosong) {any(set_kosong)}\n")

# --- 7. sorted() ---
print("--- 7. sorted() ---")
print("Fungsi sorted() akan mengembalikan list baru yang berisi semua elemen dari set yang sudah diurutkan.")
#Penting untuk dicatat bahwa sorted() mengembalikan list, bukan set, karena set sendiri tidak berurutan.
my_set_sort = {5, 2, 8, 1, 9}
sorted_list = sorted(my_set_sort)
print(f"Set asli: {my_set_sort}")
print(f"Set setelah diurutkan (dalam bentuk list): {sorted_list}")
print(f"Tipe data hasil sorted(): {type(sorted_list)}")

string_set = {'zebra', 'apple', 'banana', 'cat'}
sorted_string_list = sorted(string_set)
print(f"Set asli: {string_set}")
print(f"Set setelah diurutkan (dalam bentuk list): {sorted_string_list}\n")

print("--- Selesai ---")