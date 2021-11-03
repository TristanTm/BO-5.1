print("Welkom bij mijn beroepsopdracht, het spel gaat dadelijk beginnen. Je moet vluchten uit Afghanistan nadat de taliban jouw land en stad hebben overgenomen. \n Je komt voor verschillende keuzes te staan in dit spel waarin sommigen een goede aflopen hebben en de andere helaas niet. Succes! ")



def vraag1(): 
    vraag1 = input("\n  Nadat je te horen hebt gekregen dat de taliban jouw stad en land hebben overgenomen moet je een lastige keuze maken.  \n  A) Tijdelijk verstoppen. B) Terug vechten. C) Meteen Vluchten.\n") 
    if vraag1.lower() == "a":
        vraag2()
    elif vraag1.lower() == "b":
        vraag39()
    elif vraag1.lower() == "c":
        vraag3()


def vraag2():
    vraag2 = input("\n Je verstopt je in de schuilkelder die je had gegraven toen je het gevoel kreeg dat de taliban zou gaan winnen. \n Er is genoeg eten en drinken voor 4 weken, hopelijk is dat genoeg. \n Je komt na 4 weken je schuilkelder uit, het zonlicht verblind je tijdelijk maar het klinkt stil buiten. Het eten is op en je moet nu een keuze gaan maken.  \n A) Toch gaan vechten. B) Gaan vluchten. \n") 
    if vraag2.lower() == "a":
        vraag39()
    elif vraag2.lower() == "b":
        vraag3()

        
def vraag3(): 
    vraag3 = input("\n Oke vluchten is een goed idee, ga je het met de auto proberen of het vliegtuig? \n A) Auto. B) Vliegtuig. \n")
    if vraag3.lower() == "a":
        vraag4()
    elif vraag3.lower() == "b":
        vraag15()



def vraag4(): 
    vraag4 = input("\n  Oke je probeert het me de auto. Na een paar dagen is de grens in zicht. We moeten langs een controle post, heb je je paspoort mee? \n  A) JA. B) Nee. \n") 
    if vraag4.lower() == "a":
       vraag6()
    elif vraag4.lower() == "b":
       vraag5()



def vraag5(): 
    vraag5 = input("\n  Je rijd zo snel mogelijk langs de controle post, helaas waren ze hierop voorbereid en hadden ze een tank klaar staan. \n  Je komt langs de post alleen schiet de tank een seconde daarna je auto kapot, je sterft ter plekken. \n  A) opnieuw proberen. B) Terug naar vraag 3.\n ") 
    if vraag5.lower() == "a":
        vraag1()
    elif vraag5.lower() == "b":
        vraag3()



def vraag6(): 
    vraag6 = input("\n Top! Je moet nu alleen rustig en normaal langs de controle post. Als het goed is kan je er zo langs.  \n Geweldig! Je bent er langs we zijn nu veilig, maar waar zullen we nu naartoe?\n A) Belgie. B) Nederland. \n") 
    if vraag6.lower() == "a":
        vraag9()
    elif vraag6.lower() == "b":   
        vraag7()



def vraag7(): 
    vraag7 = input("\n  Je komt na 6 maanden reizen veilig aan in Nederland. Hier krijg je van de douane een keuze. Wil je asiel aanvragen in Noord-Holland of Friesland. \n  A) Noord-Holland. B) Friesland. \n") 
    if vraag7.lower() == "a":
        vraag10()
    elif vraag7.lower() == "b":   
        vraag8()



def vraag8(): 
    vraag8 = input("\n  Je komt in Friesland aan en wordt helaas niet geaccepteerd door de bewoners, je probeert te vluchten maar struikelt helaas en valt op de grond. \n  Een paar seconden later komt er een tank aanrijden en word je doodgeschoten. \n  A) Helemaal opnieuw. B) Terug naar vraag 7.\n") 
    if vraag8.lower() == "a":
        vraag1()
    elif vraag8.lower() == "b":   
        vraag7()



def vraag9(): 
    vraag9 = input("\n  Je komt na 6 maanden reizen veilig aan in België, helaas gebeurt hier iets onverwachts. \n  De wegen zijn zo slecht dat de auto over de kop vliegt, uit elkaar valt en explodeert hierdoor overlijdt je ter plekken. \n  A) Helemaal opnieuw. B) Terug naar vraag 6. \n") 
    if vraag9.lower() == "a":
        vraag1()
    elif vraag9.lower() == "b":   
        vraag6()



def vraag10(): 
    vraag10 = input("""\n Je komt in Noord-Holland aan en word meteen geaccepteerd door iedereen daar. 
 Je krijgt na een paar dagen wachten je paspoort en bent nu een echte burger van Nederland.
 Na een paar jaar in Nederland zijn en een goed leven opbouwen kom je iemand tegen wanneer je een dagje in Amsterdam bent.
 Hij bied je een kroket aan. Neem je deze aan of geef je toe dat je kroketten helemaal niet zo lekker vind?
 A) Accepteer de kroket en loop door
 B) Toegeven dat je kroketten niet zo lekker vind. \n """) 
    if vraag10.lower() == "a":
        vraag12() 
    elif vraag10.lower() == "b":
        vraag11() 



def vraag11(): 
    vraag11 = input("""\n De man word erg boos van dit antwoord en jullie komen hierdoor in discussie over kroketten.
 Uiteindelijk zeg je dat je frikandellen en bitterballen ook niet lekker vind, de man lijkt opeens nog bozer dan hiervoor.
 Hij haalt een klein scherp mes tevoorschijn en steekt je precies in je hart. Niemand heeft dit door in de drukte van Amsterdam en je overlijd ter plekken

 A) Opnieuw proberen
 B) Terug naar vraag 10\n""") 
    if vraag11.lower() == "a":
        vraag1()    
    elif vraag11.lower() == "b":
        vraag10()



def vraag12(): 
    vraag12 = input("""\n Je accepteerd de kroket en wil doorlopen. De man roept je terug en verteld dat dit de laatste test van de overheid was.
 Je bent geslaagd omdat je de kroket aannam. Je voelt je nu schuldig dat je niet de waarheid zei dus wat doe je nu? 
 A) Je geeft toch maar toe dat je het niet zo lekker vind
 B) Je gaat erin mee en geeft niet toe dat je het niet lekker vind  \n """) 
    if vraag12.lower() == "a":
        vraag13()
    elif vraag12.lower() == "b":
        vraag14()



def vraag13():
    vraag13 = input("\n De man vind het erg jammer om dit te horen. Hij slaat je knock out voordat je nog iets kan zeggen of doen. \n je word wakker met allemaal mensen die om je heen staan. Je weet niet waar je bent en je loop naar het eind van het dorp.\n In hoop daar iets te zien wat aangeeft waar je bent. \n Hier word je grootste angst de waarheid. Je ziet een bord waat duidelijk maakt dat je in Urk bent.  \n A) Opnieuw proberen B) Terug naar vraag 12 \n")
    if vraag13.lower() == "a":
        vraag1()
    elif vraag13.lower() == "b":
        vraag12()



def vraag14():
    vraag14 = input("\n De man feliciteerd je met het halen van de laatste test, je gaat snel naar huis en gaat door met je leven. \n Helaas leef je wel in angst dat er elke dag nog een test kan komen. \n Gefeliciteerd je hebt het gehaald!\n A) Opnieuw spelen!\n")
    if vraag14.lower() == "a":
        vraag1()



def vraag15(): 
    vraag15 = input("\nJe gaat meteen naar het vliegveld en hoopt dat je nog op tijd bent. Als je aankomt staan er veel mensen maar ook nog 5 vliegtuigen! Wat doen we nu? \nA) Proberen zonder ticket op een vliegtuig te komen. \nB) Een ticket kopen en hopen dat er genoeg plek is. \n")
    if vraag15.lower() == "a":
        vraag16()
    elif vraag15.lower() == "b":
        vraag19()



def vraag16(): 
    vraag16 = input("""\n Je rent naar het vliegtuig en probeerd door de mensen heen te komen, je ziet de deur van het vliegtuig al dicht gaan en je rent voor je leven.
 Je komt bij de deur aan en hij is al zo goed als dicht. Je baald en bent zojuist alle hoop verloren. 
 Je hebt geluk! De deur blijft vast zitten en je kan nog net naar binnen springen.
 Je krijgt aan boord te horen dat het vliegtuig naar Cuba gaat, je hebt weinig keuze en probeerd even te slapen tijdens de reis. 
 10 uur later kom je aan. Je stapt naar buiten en voelt de warmte om je heen
 Je moet weer een keuze maken, wil je hier blijven of meteen op de volgende vlucht naar Nederland? \n
 A) Blijven
 B) Nederland \n""")
    if vraag16.lower() == "a":
        vraag17()
    elif vraag16.lower() == "b":
        vraag18()



def vraag17(): 
    vraag17 = input("""\n Je blijft op Cuba maar helaas, een paar dagen na je aankomst word er een staatsgreep gepleegd door het leger.
 Overal rijden tanks en zijn soldaten, het is een grote oorlog. Je probeerd naar het vliegveld te komen om te ontsnappen.
 Helaas heb je erg veel pech, aan de ander kant van het eiland schiet een tank recht de lucht als overwinningschot. 
 Dit schot komt terug naar beneden en land dircet op jouw. Je lichaam word verpulvert en je bent meteen dood.
 A) Opnieuw proberen
 B) Terug naar vraag 16 \n""")
    if vraag17.lower() == "a":
        vraag1()
    elif vraag17.lower() == "b":
        vraag16()



def vraag18(): 
    vraag18 = input("""\n Je koop meteen een ticket voor een vlucht naar Nederland en bent snel weer onderweg.
 Je komt in Nederland aan en word meteen geaccepteerd door iedereen daar. 
 Je krijgt na een paar dagen wachten je paspoort en bent nu een echte burger van Nederland.
 Na een paar jaar in Nederland zijn en een goed leven opbouwen kom je iemand tegen wanneer je een dagje in Amsterdam bent.
 Hij bied je een kroket aan. Neem je deze aan of geef je toe dat je kroketten helemaal niet zo lekker vind?
 A) Accepteer de kroket en loop door
 B) Toegeven dat je kroketten niet zo lekker vind.  \n""")
    if vraag18.lower() == "a":
        vraag12()
    elif vraag18.lower() == "b":
        vraag11()


def vraag19(): 
    vraag19 = input("""\n Je gaat naar de balie waar gelukkig nog een werknemer is. Er zijn gelukkug nog 3 vluchten, een naar Amerika een naar Rusland en een naar Nederland. 
 A) Amerika. B) Rusland. C) Nederland.\n""")
    if vraag19.lower() == "a":
        vraag20()
    elif vraag19.lower() == "b":
        vraag36()
    elif vraag19.lower() == "c":
        vraag30()



def vraag20(): 
    vraag20 = input("""\nOke Amerika it is! Je krijgt de keuze tussen business en first class.\nA) First. B) business.  \n""")
    if vraag20.lower() == "a":
        vraag21()
    elif vraag20.lower() == "b":
        vraag22()



def vraag21(): 
    vraag21 = input("""\n Je hebt gelukkig net genoeg voor First class en kiest daar voor zodat je even kan uitrusten.
 De vliegreis is 20 uur dus je kan even lekker gaan slapen.
 Als je in amerika aankomt heb je lekker geslapen en je voelt je goed, maar wat nu? 
 A) Visa aanvragen 
 B) Gewoon zo lang mogelijk blijven en doen alsof je op vakantie bent. \n""")
    if vraag21.lower() == "a":
        vraag23()
    elif vraag21.lower() == "b":
        vraag24()



def vraag22(): 
    vraag22 = input("""\n Je wil het liefst wat geld overhouden dus je kiest voor business class. 
 Hier zit je naast een oude man die op familie bezoek was maar moest gaan vluchten voor de taliban. 
 Als je in amerika aankomt heb je lekker geslapen en je voelt je goed, maar wat nu? 
 A) Visa aanvragen 
 B) Gewoon zo lang mogelijk blijven en doen alsof je op vakantie bent.  \n""")
    if vraag22.lower() == "a":
        vraag23()
    elif vraag22.lower() == "b":
        vraag24()



def vraag23(): 
    vraag23 = input("""\n Je gaat naar de douane en doorloopt het hele proces om je visa aan te vragen. En je hebt geluk! 
 Je krijgt je visa voor iedergeval de komende 5 jaar en kan veilig je leven opbouwen in amerika. Je denk terug aan wat je allemaal hebt meegemaakt.
 Na een aantal jaar wil je een nieuwe baan, wat word het.
 A) Bull rider
 B) Spreken worden voor vluchtelingen organisatie   \n""")
    if vraag23.lower() == "a":
        vraag25()
    elif vraag23.lower() == "b":
        vraag26()



def vraag24(): 
    vraag24 = input("""\n Je bent nu al succesvol 2 jaar op "vakantie" in Amerika! Alles loopt prima en je hebt het erg naar ja zin!
 Todat er iets gebeurd wat je niet had verwacht...... Trump word president. 
 Je probeert je bestaan nog beter te verbergen zodat je niet gevonden wordt maar het is al te laat.
 De douane vind je en je word terug naar afghanistan gestuurd. 
 \n
 A) Opnieuw proberen
 B) Terug naar vraag 23  \n""")
    if vraag24.lower() == "a":
        vraag1()
    elif vraag24.lower() == "b":
        vraag23()



def vraag25(): 
    vraag25 = input("""\n Je gaat op solicitatie en word aangenomen, je blijkt een natuurtalend te zijn!
 Het bedrijf geeft je een aanbieding om naar Texas te gaan en daar professioneel bull rider te zijn. Je neemt het aan en vertrekt meteen.
 Hier maak je een grote cariere en word je een van de meest gerespecteerde mensen in Texas! 
 \n
 Gefeliciteerd je hebt het gehaald met een goed einde! Wil je toch naar een ander land of opnieuw proberen? 
 A) Ander land
 B) Opnieuw proberen   \n""")
    if vraag25.lower() == "a":
        vraag19()
    elif vraag25.lower() == "b":
        vraag1()



def vraag26(): 
    vraag26 = input("""\n Je soliciteerd bij de organisatie en word snel al aangenomen, 
 Je kan veel vertellen vanwegen eigen ervaringen en het is duidelijk dat je gemotiveerd bent om andere te helpen.   
 De baan begint met veel bellen en stukken schrijven die mensen van informatie voorzien over hoe het is als vluchteling en hoe lastig het kan zijn.
 Na een tijd werken mag je zelf ook in het veld gaan helpen. Wat wil je gaan doen? 
 A) Naar een tentenkamp om te helpen.
 B) Bij het vliegveld vluchtelingen opvangen. \n""")
    if vraag26.lower() == "a":
        vraag27()
    elif vraag26.lower() == "b":
        vraag28()



def vraag27(): 
    vraag27 = input("""\n Je vertrekt naar een van de grote tentenkampen in het Midden-Oosten en gaat daar mensen helpen.
 Hier werkt je voor 8 weken en je maakt veel dingen mee. Daarnaast help je elke dag ook veel mensen! 
 Door deze 8 weken voel je je erg goed omdat je veel mensen hebt geholpen. Je gaat hierna weer naar Amerika en leeft de rest van je leven in rust.
 \n
 Gefeliciteerd je hebt een goed einde gehaald! Wil je opnieuw proberen of naar een ander land?
 A) Opnieuw proberen
 B) Naar ander land  \n""")
    if vraag27.lower() == "a":
        vraag1()
    elif vraag27.lower() == "b":
        vraag19()



def vraag28(): 
    vraag28 = input("""\n Je gaat naar het vliegveld en vangt daar meerdere keren een groep mensen op. 
 Je helpt ze met een visa krijgen en veel andere dingen!
 Door deze hulp die je aanbied voel je je erg goed omdat je veel mensen hebt geholpen. Je gaat hierna weer naar huis en leeft de rest van je leven in rust.
 \n
 Gefeliciteerd je hebt een goed einde gehaald! Wil je opnieuw proberen of naar een ander land?
 A) Opnieuw proberen
 B) Naar ander land    \n""")
    if vraag28.lower() == "a":
        vraag1()
    elif vraag28.lower() == "b":
        vraag19()



def vraag29(): 
    vraag29 = input("""\n Je blijft in Amsterdam en word snel geaccepteerd door iedereen daar. 
 Je krijgt na een paar dagen wachten je paspoort en bent nu een echte burger van Nederland.
 Na een paar jaar in Nederland zijn en een goed leven opbouwen kom je iemand tegen wanneer je een dagje in Amsterdam bent.
 Hij bied je een kroket aan. Neem je deze aan of geef je toe dat je kroketten helemaal niet zo lekker vind?
 A) Accepteer de kroket en loop door
 B) Toegeven dat je kroketten niet zo lekker vind.  \n""")
    if vraag29.lower() == "a":
        vraag12()
    elif vraag29.lower() == "b":
        vraag11()



def vraag30(): 
    vraag30 = input("""\n Nederland word je keuze! Je krijgt de keuze tussen business en first class. 
 A) First. B) business.   \n""")
    if vraag30.lower() == "a":
       vraag31()
    elif vraag30.lower() == "b":
       vraag32()




def vraag31(): 
    vraag31 = input("""\n Je hebt gelukkig net genoeg voor First class en kiest daar voor zodat je even kan uitrusten. 
 De vliegreis is 11 uur dus jje kan even lekker gaan slapen.
 \n
 In Nederland aangekomen land je in Amsterdam. Hier ga je naar de douane die heel aardig zijn.
 Ze helpen je contact zoeken met vluchtelingen help. Vluchtelingen help  geeft je de keuze of je in de buurt van Amsterdam wil blijven of dat je naar Maastricht wil.
 A) Amsterdam. 
 B) Maastricht.      \n""")
    if vraag31.lower() == "a":
       vraag33()
    elif vraag31.lower() == "b":
       vraag34()




def vraag32(): 
    vraag32 = input("""\n Je wil het liefst wat geld overhouden dus je kiest voor business class. 
 Hier zit je naast een vrouw die op vakantie was maar moest vluchten voor de taliban. 
 Ze kan gelukkig goed Engels en samen praten jullie over Nederland. 
 \n
 In Nederland aangekomen land je in Amsterdam. Hier ga je naar de douane die heel aardig zijn.
 Ze helpen je contact zoeken met vluchtelingen help. Vluchtelingen help  geeft je de keuze of je in de buurt van Amsterdam wil blijven of dat je naar Maastricht wil.
 A) Amsterdam. 
 B) Maastricht.  \n""")
    if vraag32.lower() == "a":
       vraag33()
    elif vraag32.lower() == "b":
       vraag34()



def vraag33(): 
    vraag33 = input("""\n In Amsterdam vind je het erg gezellig maar wel heel erg druk. 
 je maakt er het beste van maar twjifelt of je misschien weg wil gaan. Toch ergens anders in Nederland? Misschien lekker zuidelijk.
 A) Maastricht
 B) In Amsterdam blijven \n""")
    if vraag33.lower() ==  "a":
       vraag34()
    elif vraag33.lower() == "b":
       vraag29()



def vraag34(): 
    vraag34 = input("""\n Eenmaal in Maastricht kom je er achter dan er heuvels zijn in Nederland en dat het niet helemaal vlak is. 
 Wil je hier blijven wonen? Zo nee dan moet je wel naar Amsterdam.
 A) Ja. 
 B) Nee.   \n""")
    if vraag34.lower() == "a":
       vraag35()
    elif vraag34.lower() == "b":
       vraag33()



def vraag35(): 
    vraag35 = input("""\n Je blijft in Maastricht en bouwt hier een mooi leven op. Je leeft de rest van je leven hier in rust.
 \n
 A) Opnieuw proberen
 B) Terug naar vraag 34  \n""")
    if vraag35.lower() == "a":
       vraag1()
    elif vraag35.lower() == "b":
       vraag34()



def vraag36(): 
    vraag36 = input("""\n Je wil meteen naar Rusland. Je stapt op het vliegtuig en mag zelf kiezen waar je wil zitten. 
 Er is een rustige plek met mensen die al slapen en een plek naast een man. 
 A) Rustige plek 
 B) Naast de man  \n""")
    if vraag36.lower() == "a":
       vraag37()
    elif vraag36.lower() == "b":
       vraag38()



def vraag37(): 
    vraag37 = input("""\n Je neemt plaats in op de rustige plek en porbeert ook evem wat slaap te pakken. 
 Na een lange vlucht kom je uitgerust aan in Rusland. Het land ziet er erg anders uit dan wat je gewend bent.
 Je komt in contact met doane die je helpen aan een paspoort. Het gaat allemaal erg snel en je bent binnen een jaar al een officiële burger.
 Na een aantal jaar ben je helemaal gewend aan het land en heb je besloten dat je de rest van je leven daar zal blijven. 
 \n
 Gefeliciteerd je hebt het uitgespeel! Wil je A) Opnieuw spelen. B) Ander land. \n""")
    if vraag37.lower() == "a":
       vraag1()
    elif vraag37.lower() == "b":
       vraag19()



def vraag38(): 
    vraag38 = input("""\n Je neemt plek naast de man en begint een goed gesprek. De man was op familie bezoek maar moest vluchten vanwegen de taliban. 
 Jullie praten grotendeels van de vlucht over familie, Rusland en veel andere dingen. De man bied je aan te helpen zodra jullie in rusland zijn.
 De man brengt je mee naar zijn huis en laat je daar overnachten. Hij helpt je aan een paspoort komen en je bent al snel een echte burger. 
 Je hebt uiteindelijk zelf een baan, huis en zelfs een vriendin, maar je blijft nog steeds vrienden met de man die je heeft geholpen.
 \n
 Gefeliciteerd je hebt het uitgespeel! Wil je A) Opnieuw spelen. B) Ander land. \n""")
    if vraag37.lower() == "a":
       vraag1()
    elif vraag37.lower() == "b":
       vraag19()



def vraag39(): 
    vraag2 = input("""\n Je maakt een plan om terug te gaan vechten tegen de taliban. Je denk dat extra mensen zoeken handig zijn, gaan we dat doen?.
 A) Extra mensen zoeken
 B) Alleen erop af gaan \n""")
    if vraag2.lower() == "a":
        vraag40()
    elif vraag2.lower() == "b":
        vraag42()




def vraag40():
    vraag40 = input("""\n Je bent gaan zoeken maar bent helaas niemand tegen gekomen die ook terug wil gaan vechten. 
 Je staat er dus alleen voor. Gaan je er alsnog op af? Of is het toch beter om te gaan vluchten.
 A) Alsnog vechten!
 B) Toch vluchten  \n""")
    if vraag40.lower() == "a":
        vraag41()
    elif vraag40.lower() == "b":
        vraag3()


def vraag41():
    vraag41 = input("""\n Je hebt al je moed verzameld en rent op een van de kampen van de Taliban af. 
 Je ziet ze al zitten wanneer er opeens uit een zijstraat een tank komt rijden. 
 De tank geeft extra gas en voordat je iets kan doen rijd de tank over je heen. Je sterft ter plekken.
 A) Een vraag terug
 B) Opnieuw proberen \n""")
    if vraag41.lower() == "a":
        vraag40()
    elif vraag41.lower() == "b":
        vraag1()



def vraag42():
    vraag42 = input("""\n Je besluit er alleen op af te gaan. Je hebt van mensen gehoord waar de Taliban aan het overnachten is. 
 Je sluipt er op af. Je ziet de ingang van een gebouw naast het kamp, je sluipt naar binnen en ziet een wapen liggen. 
 Je raapt het wapen op en er zitten nog wat kogwls in. Je ziet en trap naar boven en de uitgang. Wat doe je? 
 A) Trap naar boven om vanaf daar aan te vallen
 B) Vanaf beneden sneaky aanvallen. \n""")
    if vraag42.lower() == "a":
        vraag43()
    elif vraag42.lower() == "b":
        vraag44()



def vraag43():
    vraag43 = input("""\n Je sluipt naar boven en maakt het wapen klaar om aan te vallen. 
 Terwijl je dit doet let je helaas even niet goed op en struikel je over een steen op de trap. 
 Je maakt veel geluid wanneer je naar beneden valt en de Taliban hoort dit meteen. Ze komen op je af, 
 voordat je iets kan doen word je doodgeschoten. 
 A) Vraag terug.
 B) Opnieuw proberen.  \n""")
    if vraag43.lower() == "a":
        vraag40()
    elif vraag43.lower() == "b":
        vraag1()



def vraag44():
    vraag44 = input("""\n Je gaat het gebouw weer uit en sluipt op het kamp af. 
 Wanneer je dichterbij komt hoor je mensen praten en zie je een groot vuur waar mensen omheen staan. 
 Je spot een paar mensen helemaal aan de rand die de wacht houden, je plan is om hun eerst te pakken. 
 Terwijl je op een van de wachters af gaat sta je op een takje wat met een krak breekt. 
 Een paar mensen rond het vuur draaien zich meteen om en openen vuur. 
 Je word kritiek geraakt en overlijd ter plekken.
 A) Vraag terug.
 B) Opnieuw proberen.  \n""")
    if vraag44.lower() == "a":
        vraag40()
    elif vraag44.lower() == "b":
        vraag1()







vraag1()

