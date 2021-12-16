from googletrans import Translator, LANGUAGES
titik = '.'
en = '.en.md'
md = '.md'

translator = Translator()
text = input("Masukkan nama file : ")
bahasa = input("Terjemahkan ke Bahasa :")  

file = open(text + md, "r")
a = file.read()

hasil = translator.translate(a, dest = bahasa)

out = open(text + titik + bahasa + md, "w")

# tulis teks ke file
out.write(hasil.text)

# tutup file
out.close()

print("berhasil gan !!")
print("di simpan sebagai :", text + en) 
