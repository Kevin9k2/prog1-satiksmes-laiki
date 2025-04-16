import sqlite3 
import datetime
tagad = datetime.datetime.now()
datums = tagad.strftime("%Y-%m-%d")

def galva():
    with sqlite3.connect("satiksmes_laiki.db") as conn:
        c = conn.cursor()

        TROLLIS(c)


def TROLLIS(c):
    #c.execute(F"SELECT ") #<== Pieturu nosaukumus vaig selectot
    #atbilde = c.fetchall()
    atbilde = ["do", "re", "mi", "fa", "sol"]
    while True:
        jaut1 = input("Par kuras pieturas laikiem gribat uzzināt? Ja nezinat par kuru rakstat N: ")
        for pieturas_nosaukums in atbilde:
            pietura = pieturas_nosaukums
            if jaut1 == "N":
                jaut2 = input("TRAMVAJS\nAUTOBUSS\nTROLEJBUSS\nPar kuru transportu gribat uzzināt: ")
                if jaut2 == "TRAMVAJS":
                    while True:
                        c.execute("SELECT route_short_name FROM routes WHERE route_id LIKE \'%tram%\' ")
                        atbilde = c.fetchall()
                        trama = []
                        for rinda in atbilde:
                            for cip in rinda:
                                trama.append (cip)
                                print(f"{cip} TRAMVAJS")
                        jaut_tran = input("Par kuru tramvaju gribat uzzināt: ")
                        datu_bazite_trans(c)
                        lulala = 0
                        break
                    break
                elif jaut2 == "AUTOBUSS":
                    while True:
                        c.execute("SELECT route_short_name FROM routes WHERE route_id LIKE \'%bus%\' ")
                        atbilde = c.fetchall()
                        autot = []
                        for rinda in atbilde:
                            for cip in rinda:
                                autot.append (cip)
                                print(f"{cip} AUTOBUSS")
                        jaut_tran = input("Par kuru autobusu gribat uzzināt: ")
                        datu_bazite_trans(c)
                        lulala = 0
                        break
                    break
                elif jaut2 == "TROLEJBUSS":
                    while True:
                        c.execute("SELECT route_short_name FROM routes WHERE route_id LIKE \'%trol%\' ")
                        atbilde = c.fetchall()
                        trole = []
                        for rinda in atbilde:
                            for cip in rinda:
                                trole.append (cip)
                                print(f"{cip} TROLEJBUSS")
                        jaut_tran = input("Par kuru trolejbusu gribat uzzināt: ")
                        if jaut_tran in trole:
                            datu_bazite_trans(c)
                            lulala = 0
                            break
                        else: 
                            print("Nav tāda")
                    break
                else:
                    print("Nav tāda.")
            elif jaut1 == pietura:
                print("čiki puki")
                datu_bazite_pietura(c)
                lulala = 0
                break
            else:
                lulala = 1
        if lulala == 1:
            print("Nepareizi ievadīts vai nav tādas pieturas")
        if lulala == 0:    
            break
                






def datu_bazite_pietura(c):
    print("ciki puki")



def datu_bazite_trans(c):
    print("ciki puki")



galva()