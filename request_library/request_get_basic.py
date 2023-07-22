import requests
from collections import Counter


bolgeler_URL ="https://data.police.uk/api/forces"
response = requests.get(bolgeler_URL)

response.status_code
response.url
response.text # sonucu text olarak
response.json() # sonucu json olarak

suc_kategoriler_base_URL = "https://data.police.uk/api/crime-categories"
payload = {"date" : "2023-06"}  # kısıtlama
response = requests.get(suc_kategoriler_base_URL,payload)
response.json()


suc_base_URL = "https://data.police.uk/api/crimes-no-location"
payload = {"category" : "all-crime",
           "force" : "city-of-london",
           "date" : "2023-05"}
response = requests.get(suc_base_URL,params=payload)
response.json()


class SucRaporu():

    def __init__(self, bolge, tarih, suc_tipi="all-crime"):
        self.bolge = bolge
        self.tarih = tarih
        self.suc_tipi = suc_tipi
        self.suclar = self.suclari_bul()

    def suclari_bul(self):
        base_URL ="https://data.police.uk/api/crimes-no-location"

        payload = {"category": self.suc_tipi,
                   "force": self.bolge,
                   "date": self.tarih}
        
        response = requests.get(base_URL,params=payload)

        

        if response.status_code == 200:
            return response.json()
        else: 
            return None
    
    def suclari_raporla(self):
        suclar_listesi =[]

        if self.suclar is not None:
            for suc in self.suclar:
                suclar_listesi.append(suc["category"])
            
        return Counter(suclar_listesi)
        
suc_raporu = SucRaporu(bolge="city-of-london", tarih="2023-05",suc_tipi="all-crime")

sonuc = suc_raporu.suclari_raporla()

def list_duzenleme():
    for x in sonuc:
        print("{}\t{}\n".format(x,sonuc[x]))

list_duzenleme()
