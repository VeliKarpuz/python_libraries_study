import os

os.getcwd() #bulunduğun path

os.listdir() #klasör ve dosyaları listele

os.listdir(r"C:\Users\velik") #klasör ve dosyaları listele

os.chdir(r"C:\Users\velik\OneDrive\Documents\GitHub\python_libraries_study\os_library") #çalıştığım adres buna çevir

os.mkdir("deneme") # klasör oluştur

os.rmdir("deneme") #klasör sil

os.O_CREAT() #yeni dosya oluştur

os.O_RDONLY() #sadece oku

os.O_WRONLY() #sadece yaz

os.O_RDWR() #oku ve yaz

new_file = os.open("new_file.txt",os.O_CREAT|os.O_RDWR)
os.write(new_file, "Merhaba dünya!".encode())  #encode byte a çevirmek için
os.close(new_file)

new_file = os.open("new_file.txt",os.O_RDONLY)
istatistik =os.stat(new_file) # dosya istatistikleri/bilgileri
okunan =os.read(new_file,istatistik.st_size)  # ikinci arg kaç karakter okunacağı #st_size içerik karakter sayısı
print(okunan.decode())  # özel karakterler düzelsin diye
os.close(new_file)

# os.rename("new_file.txt","file.txt")

os.unlink("file.txt") # silme


