import re

def hitung_huruf(teks):
    """
    Menghitung jumlah total huruf dalam teks.
    Angka, tanda baca, dan spasi tidak dihitung.
    """
    jumlah_huruf = sum(1 for char in teks if char.isalpha())
    return jumlah_huruf

def hitung_kata(teks):
    """
    Menghitung jumlah total kata dalam teks.
    """
    kata_list = re.findall(r'\b\w+\b', teks.lower())
    return len(kata_list)

def hitung_kalimat(teks):
    """
    Menghitung jumlah total kalimat dalam teks.
    Asumsi: Kalimat diakhiri dengan '.', '?', atau '!'.
    """
    kalimat_list = re.split(r'[.?!]', teks)
    # Filter out empty strings that might result from splitting
    return len([kalimat for kalimat in kalimat_list if kalimat.strip()])

def hitung_paragraf(teks):
    """
    Menghitung jumlah total paragraf dalam teks.
    Asumsi: Dua karakter newline berturut-turut ('\n\n') menunjukkan akhir paragraf.
    Jika tidak ada '\n\n', anggap satu paragraf jika memiliki setidaknya tiga kalimat.
    """
    paragraf_list = teks.split('\n\n')
    valid_paragraf = [p for p in paragraf_list if p.strip()]

    if not valid_paragraf:
        return 0

    if len(valid_paragraf) == 1 and '\n\n' not in teks:
        # Check if it's a single paragraph based on sentence count
        jumlah_kalimat_dalam_teks_utuh = hitung_kalimat(teks)
        return 1 if jumlah_kalimat_dalam_teks_utuh >= 3 else 0
    
    return len(valid_paragraf)

def hitung_palindrom(teks):
    """
    Mengidentifikasi dan mengembalikan jumlah kata yang merupakan palindrom dalam teks.
    Mengabaikan tanda baca yang menempel pada kata.
    """
    palindrom_count = 0
    # Menggunakan regex untuk menemukan kata-kata, mengabaikan tanda baca
    words = re.findall(r'\b[a-zA-Z]+\b', teks.lower())
    for word in words:
        if word == word[::-1]:
            palindrom_count += 1
    return palindrom_count

def tampilkan_hasil(huruf, kata, kalimat, paragraf, palindrom):
    """
    Menampilkan hasil analisis teks dalam format yang jelas.
    """
    print(f"Jumlah huruf = {huruf}")
    print(f"Jumlah kata = {kata}")
    print(f"Jumlah kalimat = {kalimat}")
    print(f"Jumlah paragraf = {paragraf}")
    print(f"Jumlah palindrom = {palindrom}")

def main():
    """
    Fungsi utama program untuk menampilkan menu dan menjalankan analisis.
    """
    while True:
        print("\nMenu")
        print("1. Mulai Analisis Teks")
        print("2. Keluar")
        pilihan = input("Masukkan input sesuai dengan pilihan pada layar anda\n")

        if pilihan == '1':
            teks_input = input("Silakan mengetik\n")
            
            jumlah_huruf = hitung_huruf(teks_input)
            jumlah_kata = hitung_kata(teks_input)
            jumlah_kalimat = hitung_kalimat(teks_input)
            jumlah_paragraf = hitung_paragraf(teks_input)
            jumlah_palindrom = hitung_palindrom(teks_input)
            
            tampilkan_hasil(jumlah_huruf, jumlah_kata, jumlah_kalimat, jumlah_paragraf, jumlah_palindrom)
        elif pilihan == '2':
            print("Terima kasih sudah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()