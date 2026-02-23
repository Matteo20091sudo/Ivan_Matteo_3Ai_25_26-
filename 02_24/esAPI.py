#Utilizzando le API pubbliche documentate al sito https://fakeapi.net/docs/fake-e-commerce-api realizzare un programma Python che funziona nella seguente maniera:
#all'avvio il programma mostra l'elenco delle categorie di prodotti, usando l'api https://fakeapi.net/products/categories. Mostrare nel formato 
#"progressivo numerico - nome categoria". Progressivo numerico è un numero progressivo che parte da 1
#Mostrate tutte le categorie, il programma chiede quale categoria si intende visualizzare. Effettuati i dovuti controlli, vengono visualizzati
#solo gli articoli di quella specifica categoria. A tale scopo usare l'api https://fakeapi.net/products/category/....  [al posto dei puntini 
#bisogna mettere il nome della categoria scelta, ad esempio https://fakeapi.net/products/category/accessories.
#Dei prodotti va mostrato l'id, il nome ed il prezzo. 
#A quel punto il programma chiede se si vuole vedere il dettaglio di un singolo prodotto oppure tornare all'inizio (scelta categorie).
#Per visualizzare il dettaglio di un prodotto occorrerà chiamare il servizio https://fakeapi.net/products/.... [al posto dei puntini bisogna
# mettere l'id del prodotto, ad esempio https://fakeapi.net/products/1 ] 
#Nel dettaglio mostrare  id, nome, prezzo, descrizione estesa, categoria e brand.
#Alla fine si ritorna sempre all'elenco delle categorie e si riparte


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
def ScegliDettagli(ris):
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

def InserisciID(lista):
    try:
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
    except:
        print("non valido")


rifai = True
while not rifai:
    VediCategorie()
    scelta = ScelgiCategoria()
    dettagli,lista = ScegliDettagli(scelta)
    if dettagli == "s":
        InserisciID(lista)
        rifai = True
    elif dettagli == "n":
        rifai = True
    
    