import re

cumle = "Mustafa kemal Atatürk, Türk devlet adanmı, asker ve Türkiye Cumhuriyetinin kurucusudur."
patern = "Türk"

durum= re.search(patern, cumle) # ilk bulduğu sonuç gösteriliyor.
print(durum)
durum.span
durum.group
for eslesme in re.findall(patern, cumle): #findall sonuçları string olarak gösteriyor.
    print(eslesme)

for eslesme in re.finditer(patern, cumle): #findall sonuçları object olarak gösteriyor.
    print(eslesme.span(), eslesme.group(), eslesme.start(), eslesme.end())

# \d    rakam
# \D    rakam değil
# \w    karakter  (sayı veya harfleri buluyor)
# \W    karakter değil
# \s    boşluk
# \S    boşluk değil

ornek = "En sevdiğim kanal base42"
patern2 = r"base\d\d"
sonuc= re.search(patern2,ornek)
print(sonuc)

ornek2 = "Selam, benim telefon numaram 0596-552-52-66."
patern3 =r"\d\d\d\d-\d\d\d-\d\d-\d\d"
sonuc2 = re.findall(patern3,ornek2)
print(sonuc2)

# {5}        adet               aaaaa
# {3,5}      aralık             aaa aaaa
# {2,}       en az              aaaa
#  *         0 ya da fazla      x
#  +         1 ya da fazla      Ahmet1  (\w+\d)
#  ?         ya 1 ya hiç        vel     (veli?)
#  |         veya               slm|selam
#  ^         başlar             Ahmet   (^\w+)
#  $         biter              base42  (\d$)
#  .         herhangi           abcd
#  \         esc                (özel karakterden kaçmak için)    


help(re)


