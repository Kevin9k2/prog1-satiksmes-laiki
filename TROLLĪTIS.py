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
        while True:
            for pieturas_nosaukums in atbilde:
                pietura = pieturas_nosaukums
                if jaut1 == "N":
                    jaut2 = input("TRAMVAJS\nAUTOBUSS\nTROLEJBUSS\nPar kuru transportu gribat uzzināt: ")
                    if jaut2 == "TRAMVAJS":
                        #ŠEIT SARAKSTU AR TRAMVAJA NUMMURIEM
                        jaut_tran = input("Par kuru tramvaju gribat uzzināt: ")
                        datu_bazite_trans(c)
                        break
                    elif jaut2 == "AUTOBUSS":
                        #ŠEIT SARAKSTU AR AUTOBUSA NUMMURIEM
                        jaut_tran = input("Par kuru autobusu gribat uzzināt: ")
                        datu_bazite_trans(c)
                        break
                    elif jaut2 == "TROLEJBUSS":
                        #ŠEIT SARAKSTU AR TROLEJBUSA NUMMURIEM
                        jaut_tran = input("Par kuru trolejbusu gribat uzzināt: ")
                        datu_bazite_trans(c)
                        break
                elif jaut1 == pietura:
                    print("čiki puki")
                    datu_bazite_pietura(c)
                    break
            else:
                print("Nepareizi ievadīts vai nav tādas pieturas")
                #vaig lai atkārto jautajumu
            break
        break
                



def datu_bazite_pietura(c):
    #ŠEIT LAI PARADA SARAKSTU AR TAJA PIETURĀ PIENĀKOŠIEM TRANSPORTIEM ĶIP 
    jaut_tran = input("")



def datu_bazite_trans(c):
    aaaaa = 0



galva()