import requests
import json #formato
from time import sleep
def VediCategorie():
    x = requests.get("https://fakeapi.net/products/categories")
    if x.status_code!=200:
        print("Errore nel contattare il servizio online!")
    else:
        categorie = json.loads(x.text)
        g = 1
        print("CATEGORIE:")
        for i in categorie:
            print(f"{g}. {i}")
            g+=1
def ScelgiCategoria():
    x = requests.get("https://fakeapi.net/products/categories")
    if x.status_code!=200:
        print("Errore nel contattare il servizio online!")
    else:
        categorie = json.loads(x.text)
        corretto = False
        while not corretto:
            scelta = input("Inserisci la categoria che vuoi scelgiere: ").lower().strip()
            if scelta not in categorie:
                print("Scelta non valida")
            else:
                corretto = True
                return scelta
def vediProdotti(ris):
    x = requests.get(f"https://fakeapi.net/products/category/{ris}")
    if x.status_code!=200:
        print("Errore nel contattare il servizio online!")
    else:
        lista = []
        prodotti = json.loads(x.text)
        g = 1
        print(f"Prodotti della categoria {ris}:")
        for i in prodotti["data"]:
            print(f" - id: {i["id"]}, nome: {i["title"]}, prezzo: {i["price"]}€")
            lista.append(i["id"])
        corretto = False
        while not corretto:
            dettagli = input("Vuoi vedere i dettagli di un prodotto? (s/n)").strip().lower()
            if dettagli == "n":
                corretto = True
                return dettagli
            elif dettagli == "s":
                corretto = True
                return dettagli,lista
            else:
                corretto = False
                print("risposta non corretta")

def vediDettagli(lista):
    corretto = False
    while not corretto:
        id = int(input("Inserisci l'id del prodotto che desideri visualizzare: "))
        if id not in lista:
            print("Id non valido nella categoria scelta")
        else:
            corretto = True
            x = requests.get(f"https://fakeapi.net/products/{id}")
            if x.status_code!=200:
                print("Errore nel contattare il servizio online!")
            else:
                dettagli = json.loads(x.text)

                print(f"id: {dettagli["id"]};\nprezzo: {dettagli["price"]};\ndescrizione estesa: {dettagli["description"]};\nprezzo: {dettagli["price"]};\ncategoria: {dettagli["category"]};\nbrand: {dettagli["brand"]}")
                sleep(2)


rifai = False
while not rifai:
    VediCategorie()
    scelta = ScelgiCategoria()
    dettagli,lista = vediProdotti(scelta)
    if dettagli == "s":
        vediDettagli(lista)
        rifai = False
    elif dettagli == "n":
        rifai = False
    
    