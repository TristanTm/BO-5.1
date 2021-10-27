print("Welkom bij mijn beroepsopdracht, het spel gaat dadelijk beginnen. Je moet vluchten uit Afghanistan nadat de taliban jouw land en stad hebben overgenomen. \n Je komt voor verschillende keuzes te staan in dit spel waarin sommigen een goede aflopen hebben en de andere helaas niet. Succes! ")

import time

def vraag1(): 
    vraag1 = input("Nadat je te horen hebt gekregen dat de taliban jouw stan en land hebben overgenomen moet je een lastige keuze maken.  \n  A) Tijdelijk verstoppen. B) Terug vechten. C) Meteen Vluchten.") 
    if vraag1.lower() == "a":
        vraag2()
    elif vraag1.lower() == "b":
        print("HIER NOG VRAAG INVOEREN OM TE VECHTEN")
    elif vraag1.lower() == "c":
        vraag3()


def vraag2():
    vraag2 = input("Je verstopt je in de schuilkelder die je had gegraven toen je het gevoel kreeg dat de taliban zou gaan winnen. \n Er is genoeg eten en drinken voor 4 weken, hopelijk is dat genoeg. \n Je komt na 4 weken je schuilkelder uit, het zonlicht verblind je tijdelijk maar het klinkt stil buiten. Het eten is op en je moet nu een keuze gaan maken.  \n  A) Toch gaan vechten. B) Gaan vluchten. ") 
    if vraag2.lower() == "a":
        print("HIER NOG VRAAG INVOEREN OM TE VECHTEN")
    elif vraag2.lower() == "b":
        vraag3()

        
def vraag3(): 
    vraag3 = input("Oke vluchten is een goed idee, ga je het met de auto proberen of het vliegtuig? A) Auto. B) Vliegtuig. ")
    if vraag3.lower() == "a":
        vraag4()
    elif vraag3.lower() == "b":
        print("DIT IS NOG NIET AF")


def vraag4(): 
    vraag4 = input("Oke je probeert het me de auto. Na een paar dagen is de grens in zicht. We moeten langs een controle post, heb je je paspoort mee? \n  A) JA. B) Nee. ") 
    if vraag4.lower() == "a":
       vraag6()
    elif vraag4.lower() == "b":
       vraag5()



def vraag5(): 
    vraag5 = input("Je rijd zo snel mogelijk langs de controle post, helaas waren ze hierop voorbereid en hadden ze een tank klaar staan. \n  Je komt langs de post alleen schiet de tank een seconde daarna je auto kapot, je sterft ter plekken. \n  A) opnieuw proberen. B) Terug naar vraag 3. ") 
    if vraag5.lower() == "a":
        vraag1()
    elif vraag5.lower() == "b":
        vraag3()



def vraag6(): 
    vraag6 = input("Top! Je moet nu alleen rustig en normaal langs de controle post. Als het goed is kan je er zo langs. \n  Geweldig! Je bent er langs we zijn nu veilig, maar waar zullen we nu naartoe? A) Nederland. B) Belgie. ") 
    if vraag6.lower() == "a":
        vraag7()
    elif vraag6.lower() == "b":   
        vraag9()



def vraag7(): 
    vraag7 = input("Je komt na 6 maanden reizen veilig aan in Nederland. Hier krijg je van de douane een keuze. Wil je asiel aanvragen in Noord-Holland of Friesland. \n  A) Noord-Holland. B) Friesland. ") 
    if vraag7.lower() == "a":
        vraag10()
    elif vraag7.lower() == "b":   
        vraag8()



def vraag8(): 
    vraag8 = input("Je komt in Friesland aan en wordt helaas niet geaccepteerd door de bewoners, je probeert te vluchten maar struikelt helaas en valt op de grond. Een paar seconden later komt er een tank aanrijden en word je doodgeschoten. \n  A) Helemaal opnieuw. B) Terug naar vraag 7.") 
    if vraag8.lower() == "a":
        vraag1()
    elif vraag8.lower() == "b":   
        vraag7()



def vraag9(): 
    vraag9 = input("Je komt na 6 maanden reizen veilig aan in België, helaas gebeurt hier iets onverwachts. De wegen zijn zo slecht dat de auto over de kop vliegt, uit elkaar valt en explodeert hierdoor overlijdt je ter plekken. \n  A) Helemaal opnieuw. B) Terug naar vraag 6. ") 
    if vraag9.lower() == "a":
        vraag1()
    elif vraag9.lower() == "b":   
        vraag6()



def vraag10(): 
    vraag10 = input("""Je komt in Noord-Holland aan en word meteen geaccepteerd door iedereen daar. 
 Je krijgt na een paar dagen wachten je paspoort en bent nu een echte burger van Nederland.
 Na een paar jaar in Nederland zijn en een goed leven opbouwen kom je iemand tegen wanneer je een dagje in Amsterdam bent.
 Hij bied je een kroket aan. Neem je deze aan of geef je toe dat je kroketten helemaal niet zo lekker vind?
 A) Accepteer de kroket en loop door
 B) Toegeven dat je kroketten niet zo lekker vind.  """) 
    if vraag10.lower() == "a":
        vraag12() 
    elif vraag10.lower() == "b":
        vraag11() 



def vraag11(): 
    vraag11 = input("""De man word erg boos van dit antwoord en jullie komen hierdoor in discussie over kroketten.
 Uiteindelijk zeg je dat je frikandellen en bitterballen ook niet lekker vind, de man lijkt opeens nog bozer dan hiervoor.
 Hij haalt een klein scherp mes tevoorschijn en steekt je precies in je hart. Niemand heeft dit door in de drukte van Amsterdam en je overlijd ter plekken

 A) Opnieuw proberen
 B) Terug naar vraag 10""") 
    if vraag11.lower() == "a":
        vraag1()    
    elif vraag11.lower() == "b":
        vraag10()



def vraag12(): 
    vraag12 = input("""Je accepteerd de kroket en wil doorlopen. De man roept je terug en verteld dat dit de laatste test van de overheid was.
    Je bent geslaagd omdat je de kroket aannam. Je voelt je nu schuldig dat je niet de waarheid zei dus wat doe je nu? 
    A) Je geeft toch maar toe dat je het niet zo lekker vind
    B) Je gaat erin mee en geeft niet toe dat je het niet lekker vind   """) 
    if vraag12.lower() == "a":
        vraag13()
    elif vraag12.lower() == "b":
        vraag14()



def vraag13():
    vraag13 = input("De man vind het erg jammer om dit te horen. Hij slaat je knock out voordat je nog iets kan zeggen of doen. \n je word wakker met allemaal mensen die om je heen staan. Je weet niet waar je bent en je loop naar het eind van het dorp. In hoop daar iets te zien wat aangeeft waar je bent. \n Hier word je grootste angst de waarheid. Je ziet een bord waat duidelijk maakt dat je in Urk bent.  \n A) Opnieuw proberen B) Terug naar vraag 12 ")
    if vraag13.lower() == "a":
        vraag1()
    elif vraag13.lower() == "b":
        vraag12()



def vraag14():
    vraag14 = input(" De man feliciteerd je met het halen van de laatste test, je gaat snel naar huis en gaat door met je leven. \n Helaas wel in angst dat er elke dag nog een test kan komen. \n Gefeliciteerd je hebt het gehaald! A) Opnieuw spelen!")
    if vraag14.lower() == "a":
        vraag1()






vraag1()
