print ("Pendaftaran Lomba Cerdas Cermat")
umur = int(input("Masukkan umur kamu: "))
kelas = input("Masukkan kelas kamu (10/11/12): ")
pelatihan = input("Apakah kamu sudah ikut pelatihan? (ya/tidak): ").lower( )

if umur >= 15:
    # Cek syarat 2: kelas
    if kelas == "10" or kelas =="11":
        # Cek syarat 3: Pelatihan
        if pelatihan == "ya":
            print("Selamat! Kamu boleh ikut lomba cerdas cermat")
        else:
            print("Maaf, kamu harus mengikuti pelatihan terlebih dahulu")
    else:
        print("Maaf, hanya kelas 10 dan 11 yang boleh ikut.")
else: 
    print("Maaf, umur kamu belum cukup>")