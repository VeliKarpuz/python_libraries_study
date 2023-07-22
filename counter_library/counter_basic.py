from collections import Counter
import random

list1 = random.sample(range(10),k=5)
list2 = random.sample(range(10),k=5)
list3 = random.sample(range(10),k=5)
list4 = random.sample(range(10),k=5)

liste_listesi=[list1,list2,list3,list4]
list_toplam= list1 + list2 + list3 + list4

for index , liste in enumerate(liste_listesi):
    print("{}.liste \t {}".format(index+1,liste))
print(Counter(list_toplam))  #listenin içinde hangi elemandan kaç tane olduğunu sayıyor.