#Realizzare un programma Python per collezionare i film 
# visti. Memorizzare solo il nome del film. Fare in modo
#  che si possa inserire, modificare, visualizzare e 
# cancellare un film. Il programma deve anche salvare
#  i film su file e ricaricarli all'avvio.

NOME_FILE = "./03_12/film.txt"

film = []

def stampaMenu():
    print("---------ARCHIVIO-FILM--------")
    print("1. inserisci un nuovo film")
    print("2. modifica il nome di un film")
    print("3. visualizza i film nell'archivio")
    print("4. cancella un film")
    print("0. termina programma")
    print("------------------------------")
    scelta = int(input("Inserisci la tua scelta: "))
    return scelta

def carica():
    try:
        file = open(NOME_FILE, "r")
        
        righe = file.read()
        righe = righe.split("\n")
        righe.pop(-1)
        file.close()
        return righe
    except:
        print("Impossibile caricare il file dell'archivio del film")
        return []   


def salva(l):
    file = open(NOME_FILE, "w")
    for f in l:
        file.write(f + "\n")
    file.close()

def inserisciFilm(l):
    corretto = False
    while not corretto:
        nome = input("Inserisci il nome del film da inserire: ")
        if len(nome) < 2:
            print("Ciò che hai inserito è troppo corto o vuoto")
        elif nome in l:
            print("Film già presente")
        else:
            l.append(nome)
            corretto = True

def visualizzaFilm(l):
    print("--------ARCHIVIO-FILM--------")
    for c,i in enumerate(l):
        print(f"{c+1}. {i}")
    
def modificaFilm(l):
    if len(l) == 0:
        print("Archivio vuoto, nessun film da modificare")
    else:
        visualizzaFilm(l)
        corretto = False
        while not corretto:
            try:
                modifica = int(input("Inserisci il numero relativo al film: "))
                if modifica > len(l):
                    print("Non puoi inserire un numero maggiore dell'archivio")
                elif modifica < 1:
                    print("Il numero non può essere 0 o minore di esso")
                else:
                    indice = l.index(l[modifica-1])
                    nuovoNome = input("Inserisci il nuovo nome del film: ")
                    if len(nome) < 2:
                        print("Ciò che hai inserito è troppo corto o vuoto")
                    else:
                        l[indice] = nuovoNome
                        corretto = True
            except:
                print("Formato non valido")

def eliminaFilm(l):
    if len(l) == 0:
        print("Archivio vuoto, nessun film da modificare")
    else:
        visualizzaFilm(l)
        corretto = False
        while not corretto:
            try:
                elimina = int(input("Inserisci il numero relativo al film che vorresti eliminare: "))
                if elimina > len(l):
                    print("Non puoi inserire un numero maggiore dell'archivio")
                elif elimina < 1:
                    print("Il numero non può essere 0 o minore di esso")
                else:
                    indice = l.index(l[elimina-1])
                    l.pop(indice)
                    corretto = True
            except:
                print("Formato non valido")

film = carica()
esci = False
while not esci:
    scelta = stampaMenu()
    if scelta == 1:
        inserisciFilm(film)
    elif scelta == 2:
        modificaFilm(film)
    elif scelta == 3:
        visualizzaFilm(film)
    elif scelta == 4:
        eliminaFilm(film)
    elif scelta == 0:
        salva(film)
        print("CIAO CIAO!!!")
        esci = True
    else:
        print("Scelta non valida")
    
    
