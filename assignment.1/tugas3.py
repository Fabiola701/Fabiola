print("Menu:")
print("A. Tampilkan 'Computer Programming' 10x")
print("B. Tampilkan 'Bimbingan Belajar' 5x")
print("C. Akhir")

choice = input ("Pilih (A/B/C): ")

if choice == "A":
    for i in range(10):
        print("Computer Programming")
elif choice == "B":
    for i in range (5):
        print("Bimbingan belajar")
elif choice == "C":
    print("Program berakhir")
else:
    print("idk theres no choice")
