#Ohjelman tarkoituksena on tarjota käyttäjälle mahdollisuus valita auto, jonka voi tuunata
#Käyttäjälle arvotaan budjetti, jolla hän voi autoaan korjailla ja tuunata
#Käyttäjälle ilmoitetaan lista korjattavista/tuunattavista asioista, jotka korjaamalla asian saa aina poistettua listalta
#Korjattavalla/tuunattavalla asialla on aina kolme (3) vaihtoehtoa, jotka ovat eri hintaisia
#Käyttäjän pitää siten harkita käyttääkö miten paljon rahaa mihinkin asiaan

#Kerrotaan käyttäjälle simulaattorin idea ja autovaihtoehdot

from random import randrange


print("Hei, tervetuloa autontuunaussimulaattoriin!")
print("Annan sinulle viisi (5) autoa, joista valitset yhden.")
input("Jatka >")
print("1. Mazda MX-5 1990")
print("2. Saab 900 turbo 1989")
print("3. BMW E34 1996")
print("4. Nissan Micra 1995")
print("5. Volkswagen Jetta 1995")

#Kysytään käyttäjältä minkä auton hän valitsee, ja tallennetaan se muuttujaksi
print("Minkä valitset?")
valinta = input("> ")

if(valinta) == '1':
    print("Valitsit Mazda MX-5 vuosimallia 1990. Oiva valinta!")
if(valinta) == '2':
    print("Valitsit Saab 900 turbon vuodelta 1989. Mielenkiintoista!")
if(valinta) == '3':
    print("Valitsit BMW E34 vuodelta 1996. Et sinä niitä naisia tälläkään saa.")
if(valinta) == '4':
    print("Valitsit Nissan Micran vuosimallia 1995. Luuletko pystyväsi tekemään tälle jotain?")
if(valinta) == '5':
    print("Valitsit Volkswagen Jetan vuodelta 1995. Oletko muka kuullut tästä?")

input("Jatka >")

#Kysytään haluttu budjetti
print("Nyt sinä olet valinnut autosi. Haluatko että 1. Sinulla arvotaan budjetti vai 2. Määrität itse budjettisi?")
budjetti = input()
if(budjetti) == '1':
    print("Haluat että budjettisi arvotaan. Arvonta suoritetaan väliltä 1000-10 000")
    summa = randrange(1000,10000)
    print("Arvottu budjettisi on", summa)
if(budjetti) == '2':
    print("Haluat määritellä itse budjettisi. Valitse summa 1000 - 10 000 väliltä.")
    summa = input()
    print("Budjettisi on", summa)

input("Jatka >")
#Kerrotaan käyttäjälle korjattavat asiat, joista käyttäjä voi valita haluamansa osat

print("Tässä asioita, joita voit tuunata. Syöttämällä aihion numeron saat haluamastasi aiheesta vaihtoehdot.")
osat = ["1. Spoileri", "2. Lasien tummennus", "3. Vanteet", "4. Äänentoistolaitteet", "5. Kuljettajan mukavuudet"] 
print(osat)
osa = input("Syötä numero > ")

if(osa) == '1':
    print("Haluat ostaa autoosi uuden spoilerin, tässä vaihtoehdot:")
    print(" 1. 326 Power Style Spoileri 399 €")
    print(" 2. Hiilikuituspoileri 'GT style' 550 € ")
    print(" 3. Hiilikuituspoileri 'Snake style' 700 €")
    
    osa = (1,2,3)
    print("Valitse haluamasi spoileri syöttämällä sen numero")
    spoilerihinta = int(input("> "))
def uusihinta():
    summa=(summa-spoilerihinta)
    print("Budjettiasi on jäljellä", summa)
    osat.remove("1. Spoileri")
    input("Jatka > ")


print("Jatketaan tuunausta! Valitse seuraava kohta.")
print(osat)
osa = input("Syötä numero > ")


if(osa) == '2':
    print("Haluat siis tummentaa autosi lasit, tässä vaihtoehdot:")
    print(" 1. Musta spraymaali 0 €")
    print(" 2. Pelkät kalvot, asenna itse 150 €")
    print(" 3. Kalvot ja asennus 300 €")
    print("Valitse tummennus syöttämällä sen hinta.")
    tummennushinta = int(input("> "))
    summa = (summa-tummennushinta)
    print("Budjettiasi on jäljellä", summa)
    osat.remove("2. Lasien tummennus")
    input("Jatka >")

print("Jatketaan tuunausta! Valitse seuraava kohta.")
print(osat)
osa = input("Syötä numero > ")

if(osa) == '3':
    print("Aika laittaa mintit vanteet alle, tässä vaihtoehdot:")
    print(" 1. Jack Wheeler 40 € €")
    print(" 2. Barzetta Azure Dark 130 €")
    print(" 3. Barzetta GTR Gold 230 €")
    print("Valitse haluamasi vannetyyppi syöttämällä sen hinta")
    vannehinta = int(input("> "))
    summa=(summa-vannehinta)
    print("Budjettiasi on jäljellä", summa)
    osat.remove("3. Vanteet")
    input("Jatka > ")

print("Jatketaan tuunausta! Valitse seuraava kohta.")
print(osat)
osa = input("Syötä numero > ")

if(osa) == '4':
    print("Aika hifistellä, mitkä popit autoon laitetaan:")
    print(" 1. Mummon kasettisoitin 0 €")
    print(" 2. Pioneer triaksaalikaiutin 65 €")
    print(" 3. ESX AUDIO QXB12 koteloitu subwoofer + SXE2800.1D 735 €")
    print("Valitse haluamasi äänentoistojärjestelmä syöttämällä sen hinta")
    äänihinta = int(input("> "))
    summa=(summa-äänihinta)
    print("Budjettiasi on jäljellä", summa)
    osat.remove("4. Äänentoistolaitteet")
    input("Jatka > ")

print("Jatketaan tuunausta! Valitse seuraava kohta.")
print(osat)
osa = input("Syötä numero > ")

if(osa) == '5':
    print("Tehdään kuskin olo mukavaksi jollain lisämukavuudella:")
    print(" 1. Bilteman mukiteline 2 €")
    print(" 2. Wunderbaum 6 €")
    print(" 3. GPS-laite 70 €")
    print("Valitse lisämukavuus syöttämällä sen hinta.")
    mukavahinta = int(input("> "))
    summa = (summa-mukavahinta)
    print("Budjettiasi on jäljellä", summa)
    osat.remove("5. Kuljettajan mukavuudet")
    input("Jatka >")

#Määritetään lopettaminen
print("Oletko tyytyväinen autoosi, kyllä vai ei?")
while True:
    vastaus = input("> ")
    if vastaus == 'kyllä':
        break

print("Onnistuit laittamaan autosi täydellisesti kuntoon! Budjettia jäi", summa)
if(summa <0):
    print("Aijaiji, budjetti jäi miinukselle. Jäit Makelle velkaa")
else:(print("Budjettisi jäi plussalle!"))