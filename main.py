persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25,
}

run = True
operazioni = ("aggiungere", "modificare", "eliminare", "stop")


def start():
    global run
    operazione = input("Cosa vuoi fare? ")
    if operazione == operazioni[0]:
        # x = input("aggiumgi chiave:valore separati da una virgola: ")
        x = input("aggiungi chiave:valore separati dai duepunti, separare più coppie o più valori con una virgola: ")
        aggiungi(x)
    elif operazione == operazioni[1]:
        x = input("Inserire la chiave da modificare ed il nuovo valore, separati da una virgola: ")
        modifica(x.split(","))
    elif operazione == operazioni[2]:
        x = input("Inserire la chiave da eliminare: ")
        elimina(x)
    elif operazione == operazioni[3]:
        run = False


def aggiungi(param):
    x=param.split(":")
    if len(x) == 2:
        if len(x[1].split(",")) > 1:
            persona[x[0]] = list(x[1].split(","))
        else:
            persona[x[0]] = x[1]
    else:
        persona[x[0]] = dict()
        x=param.split(":",1)
        x=x[1].split(",")
        for i in range(len(x)):
            y = x[i].split(":")
            (persona[param.split(":")[0]])[y[0]] = y[1]

    print(persona)


def modifica(param):
    aggiungi(param)


def elimina(param):
    try:
        persona.pop(param)
    except:
        print("Chiave non valida")
    finally:
        print(persona)


while run:
    start()
