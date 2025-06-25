print ("Pendaftaran Lomba Cerdas Cermat")
umur = int(input("Masukkan umur kamu: "))
if umur < 15:
    print("Maaf, anda tidak bisa ikut cerdas cermat.")
else:
    kelas = input("Masukkan kelas kamu (10/11/12): ")
    if kelas != "10" and kelas != "11":
        print("Maaf, anda tidak bisa ikut cerdas cermat.")
    else:
        pelatihan = input("Apakah kamu sudah ikut pelatihan? (ya/tidak): ").lower()
        if pelatihan != "ya":
            print("Maaf, anda tidak bisa ikut cerdas cermat.")
        else:
            print("Selamat! Kamu boleh ikut lomba cerdas cermat.")
