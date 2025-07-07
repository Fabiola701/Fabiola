string1 = "heLLo, selamat datang di DUNIA pemrograman python! !"

cleaned_string = string1.strip().lower()
cleaned_string = cleaned_string.capitalize()

print(f"result after cleaned: {cleaned_string}")

# Potong & Gabung
python_awal_index = cleaned_string.find("python")
if python_awal_index != -1:
    sliced_python = cleaned_string[python_awal_index : python_awal_index + len("python")]
else:
    sliced_python = "python"

print(f"python yang dipotong: {sliced_python}")

combinedString = "Selamat datang di" + " " + sliced_python.capitalize()

print(f"combinedString: {combinedString}")

twoPythons = sliced_python.capitalize() * 2

print(f"2Pythons: {twoPythons}")

# Format dan Cek Keanggotaan:

kalimatno1 = "{} adalah bahasa yang akan saya kuasai dalam {} tahun."
kalimatno2 = kalimatno1.format("Python", 2)

print(f"kalimat: {kalimatno2}")

adaNdaKuasai = "kuasai" in kalimatno2
print(f"Apakah kata Kuasai ada di dalam kalimat? {adaNdaKuasai}")

adaNdaJava = "java" not in kalimatno2
print(f"Apakah kata Java tidak ada di dalam kalimat? {adaNdaJava}")

