import random

# Fungsi untuk menghasilkan angka acak dari 1 dan 100
def generate_random_number():
    """
    Menghasilkan bilangan bulat acak antara 1 dan 100 (inklusif).
    """
    return random.randint(1, 100)

# Fungsi untuk mendapatkan tebakan pengguna dan memvalidasinya
def get_user_guess():
    """
    Meminta pengguna untuk memasukkan tebakan dan memvalidasi apakah itu bilangan bulat.
    Terus meminta masukan sampai masukan yang valid diterima.
    """
    while True: # Loop while untuk memastikan masukan bilangan bulat yang valid
        try:
            guess = int(input("Masukkan tebakan Kamu (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Tebakan Kamu di luar jangkauan. Silakan tebak angka antara 1 dan 100.")
        except ValueError:
            print("Masukan tidak valid. Silakan masukkan angka bulat.")


# Fungsi untuk memainkan satu putaran permainan
def play_game():
    """
    Berisi logika utama untuk satu putaran permainan tebak angka.
    Ini menghasilkan angka acak, menangani tebakan pengguna, dan memeriksa kondisi menang/kalah.
    """
    secret_number = generate_random_number()
    attempts = 0
    max_attempts = 10
    has_won = False

    print("\nSaya sedang memikirkan angka antara 1 dan 100.")
    print(f"Kamu punya {max_attempts} percobaan untuk menebaknya.")

    # Loop for untuk membatasi jumlah percobaan
    for attempt in range(1, max_attempts + 1):
        print(f"\nPercobaan {attempt}/{max_attempts}")
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("Terlalu rendah! Coba lagi.")
        elif guess > secret_number:
            print("Terlalu tinggi! Coba lagi.")
        else:
            print(f"\nSelamat! Kamu menebak angka {secret_number} dalam {attempts} percobaan.")
            has_won = True
            break # Keluar dari loop for jika angka berhasil ditebak

    if not has_won:
        print(f"\nPermainan berakhir! Kamu kehabisan percobaan.")
        print(f"Angka rahasianya adalah: {secret_number}")

    # Mengembalikan apakah pengguna menang atau kalah
    return has_won

# Fungsi utama untuk mengontrol alur permainan dan loop "main lagi"
def main():
    """
    Fungsi utama yang mengatur permainan.
    Ini mencakup loop while untuk memungkinkan pengguna memainkan beberapa putaran.
    """
    play_again = True
    # Loop while untuk terus bermain sampai pengguna berhenti
    while play_again:
        # Mainkan satu putaran permainan
        play_game()

        # Loop while dalam untuk masukan "main lagi" yang valid
        while True:
            choice = input("Apakah Kamu ingin bermain lagi? (ya/tidak): ").lower().strip()
            if choice == "ya":
                play_again = True
                # Keluar dari loop dalam, lanjutkan loop permainan luar
                break
            elif choice == "tidak":
                play_again = False
                # Keluar dari loop dalam, lalu loop permainan luar
                break
            else:
                print("Masukan tidak valid. Silakan ketik 'ya' atau 'tidak'.")

    print("\nTerima kasih sudah bermain! Bye-bye.")

# Titik masuk program
if __name__ == "__main__":
    main() # Panggil fungsi utama untuk memulai permainan




    




