print("Welkom bij mijn beroepsopdracht, het spel gaat dadelijk beginnen")





def vraag1(): 
    vraag1 = input("Je woont in Afghanistan en de taliban heeft de stad overgenomen wat ga je doen?  \n  A) Tijdelijk verstoppen. B) Terug vechten. C) Meteen Vluchten.") 
    if vraag1.lower() == "a":
        vraag2()
    elif vraag1.lower() == "b":
        print("HIER NOG VRAAG INVOEREN OM TE VECHTEN")
    elif vraag1.lower() == "c":
        vraag3()


def vraag2():
    vraag2 = input("Oke je verstopt je in een schuilkelder en je komt er later weer uit. \n  Het is 3 weken later en je eten is bijna op je moet een keuze gaan maken. \n  A) Toch gaan vechten. B) Gaan vluchten. ") 
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
        print("hier noord holland verderlaten gaan")
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





vraag1()