import random

random.random() # 0-1 arası 
random.uniform(5,10) # aralık
random.randint(5,10) # aralık arası int

print(random.randint(5,10))
sayi = random.randint(5,10)
print(sayi)

liste = [*range(10)]

random.choice(liste)  # listede rastgele eleman seçme
random.sample(liste, k=3)  # listeden istenen miktarda rasgele elman seçme
random.shuffle(liste)  # listeyi karıştırma

