import sqlite3 
import datetime
tagad = datetime.datetime.now()
datums = tagad.strftime("%Y-%m-%d")

def galva():
    with sqlite3.connect("satiksmes_laiki.db") as conn:
        c = conn.cursor()

        TROLLIS(c)


def TROLLIS(c):
    z = 0
    c.execute("SELECT stop_name FROM stops")
    atbilde = c.fetchall()
    pieturas = [rinda[0].strip().lower() for rinda in atbilde]
    while True:
        jaut1 = input("Ja zinat kuru pieturu, rakstat pieturu, Ja nezinat par kuru rakstat n: ").strip().lower()
        for pieturas_nosaukums in atbilde:
            pietura = pieturas_nosaukums
            if jaut1 == "n":
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
                        if jaut_tran in trama:
                            z = 1
                            x = datu_bazite_trans(c, jaut_tran, z)
                            lulala = 0
                            g = 2
                            BEIGAS(x, g, z, jaut_tran, jaut1)
                            break
                        else: 
                            print("Nav tāda")
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
                        if jaut_tran in autot:
                            z = 2
                            x = datu_bazite_trans(c, jaut_tran, z)
                            lulala = 0
                            g = 2
                            BEIGAS(x, g, z, jaut_tran, jaut1)
                            break
                        else: 
                            print("Nav tāda")
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
                            z = 3
                            x = datu_bazite_trans(c, jaut_tran, z)
                            lulala = 0
                            g = 2
                            BEIGAS(x, g, z, jaut_tran, jaut1)
                            break
                        else: 
                            print("Nav tāda")
                    break
                else:
                    print("Nav tāda.")
            elif jaut1 in pieturas:
                print("fire")
                x = datu_bazite_pietura(c, jaut1) # x-- (viena, otra, tr, cet)
                lulala = 0
                g = 1
                BEIGAS(x, g, z, jaut_tran, jaut1)
                break
            else:
                lulala = 1
        if lulala == 1:
            print("Nepareizi ievadīts vai nav tādas pieturas")
        if lulala == 0:    
            break
    
                

def datu_bazite_pietura(c, jaut1):
    jaut1 = jaut1.capitalize()
    print(jaut1)
    transporte = input("Ievadiet, kādu transportu veidu jums vajag (bus, tram, trol): ")
    if transporte not in ('bus', 'tram', 'trol'):
        print("Nepareizs transporta veids!")
        return
    numbero = int(input("Ievadiet tā transporta ciparu, kuru jums vajag: "))
    celo = int(input("Turp vai atpakaļ? (0 vai 1): "))
    if celo not in (0, 1):
        print("Nepareiza virziena izvēle!")
        return
    
    c.execute(f"""
        SELECT stop_times.arrival_time 
        FROM stop_times
        JOIN stops ON stop_times.stop_id = stops.stop_id
        JOIN trips ON stop_times.trip_id = trips.trip_id
        JOIN routes ON trips.route_id = routes.route_id
        WHERE stops.stop_name = '{jaut1}'
        AND trips.direction_id = {celo}
        AND routes.route_id LIKE '%{transporte}%'
        AND routes.route_short_name = {numbero}
    """)
    
    atbilde = c.fetchall()
    return atbilde, numbero, transporte



def datu_bazite_trans(c, jaut_tran, z):
    if z == 1:
        c.execute(f"""
            SELECT DISTINCT stops.stop_name 
            FROM stops
            JOIN stop_times ON stops.stop_id = stop_times.stop_id
            JOIN trips ON stop_times.trip_id = trips.trip_id
            JOIN routes ON trips.route_id = routes.route_id
            WHERE routes.route_short_name = {jaut_tran}
            AND routes.route_id LIKE \'%tram%\'
        """)
        atbilde = c.fetchall()
        for rinda in atbilde:
            print(rinda)
        while True:
            jaut1 = input(" Kuru pieturu ").strip().lower()
            jaut1 = jaut1.capitalize()
            if jaut1 in atbilde:
                break
            
        celo = int(input("Turp vai atpakaļ? (0 vai 1): "))
        if celo not in (0, 1):
            print("Nepareiza virziena izvēle!")
            return
        c.execute(f"""
        SELECT stop_times.arrival_time 
        FROM stop_times
        JOIN stops ON stop_times.stop_id = stops.stop_id
        JOIN trips ON stop_times.trip_id = trips.trip_id
        JOIN routes ON trips.route_id = routes.route_id
        WHERE stops.stop_name = '{jaut1}'
        AND trips.direction_id = {celo}
        AND routes.route_id LIKE '%tram%'
        AND routes.route_short_name = {jaut_tran}
        """)
        atbilde = c.fetchall()
        return atbilde, jaut1
    elif z == 2:
        c.execute(f"""
            SELECT DISTINCT stops.stop_name 
            FROM stops
            JOIN stop_times ON stops.stop_id = stop_times.stop_id
            JOIN trips ON stop_times.trip_id = trips.trip_id
            JOIN routes ON trips.route_id = routes.route_id
            WHERE routes.route_short_name = {jaut_tran}
            AND routes.route_id LIKE \'%bus%\'
        """)

        atbilde2 = c.fetchall()
        for rinda in atbilde2:
            print(rinda)
        jaut1 = input(" Kuru pieturu ").strip().lower()
        jaut1 = jaut1.capitalize()
        celo = int(input("Turp vai atpakaļ? (0 vai 1): "))
        if celo not in (0, 1):
            print("Nepareiza virziena izvēle!")
            return
        c.execute(f"""
        SELECT stop_times.arrival_time 
        FROM stop_times
        JOIN stops ON stop_times.stop_id = stops.stop_id
        JOIN trips ON stop_times.trip_id = trips.trip_id
        JOIN routes ON trips.route_id = routes.route_id
        WHERE stops.stop_name = '{jaut1}'
        AND trips.direction_id = {celo}
        AND routes.route_id LIKE '%bus%'
        AND routes.route_short_name = {jaut_tran}
        """)
        atbilde = c.fetchall()
        return atbilde, jaut1
    elif z == 3:
        c.execute(f"""
            SELECT DISTINCT stops.stop_name 
            FROM stops
            JOIN stop_times ON stops.stop_id = stop_times.stop_id
            JOIN trips ON stop_times.trip_id = trips.trip_id
            JOIN routes ON trips.route_id = routes.route_id
            WHERE routes.route_short_name = {jaut_tran}
            AND routes.route_id LIKE \'%trol%\'
        """)

        atbilde3 = c.fetchall()
        for rinda in atbilde3:
            print(rinda)
        jaut1 = input(" Kuru pieturu ").strip().lower()
        jaut1 = jaut1.capitalize()
        celo = int(input("Turp vai atpakaļ? (0 vai 1): "))
        if celo not in (0, 1):
            print("Nepareiza virziena izvēle!")
            return
        c.execute(f"""
            SELECT stop_times.arrival_time 
            FROM stop_times
            JOIN stops ON stop_times.stop_id = stops.stop_id
            JOIN trips ON stop_times.trip_id = trips.trip_id
            JOIN routes ON trips.route_id = routes.route_id
            WHERE stops.stop_name = '{jaut1}'
            AND trips.direction_id = {celo}
            AND routes.route_id LIKE '%trol%'
            AND routes.route_short_name = {jaut_tran}
        """)
        atbilde = c.fetchall()
        return atbilde, jaut1
    else:
        print("ej tu kaka")





def BEIGAS(x, g, z, jaut_tran, jaut1):
    if g == 1:
        if x[2] == "bus":
            tran = "Autobuss"
        elif x[2] == "tram":
            tran = "Tramvajs"
        elif x[2] == "trol":
            tran = "Trolejbuss"
        print (f"{x[1]} {tran} laiki {jaut1} pieturā")
        for rinda in x[0]:
            print(rinda)
    elif g == 2:
        if z == 1:
            tran = "Tramvajs"
        elif z == 2:
            tran = "Autobuss"
        elif z == 3:
            tran = "Trolejbuss"
        print (f"{jaut_tran} {tran} laiki {x[1]} pieturā")
        for rinda in x[0]:
            print(rinda)


galva()
