# An_unexpected_Journey_Bernd_Kuebrich

# Warum dieses Spiel?
Da ich schon über 15 Jahren ein rießiger Fan von Rollenspiel/Adventures der Marke "Zelda" bin dachte ich mir es ist bestimmt interessant heraus zu finden 
wieviel Arbeit eigentlich dahinter steckt.
Und ich habe festgestellt, der Aufwand ist rießig und eigentlich braucht man auch einen Grafiker.  

# Das Spiel
Zuerst landet man in einem kleinen Menü in dem man das Spiel starten kann.  
Die Hauptfigur hat die Aufgabe, in der Spielwelt verteilte Items zu finden und aufzusammeln und damit den fießen Gegner Ganon zu besiegen.  
Die Spielwelt besteht aus 3 verbundenen Levels. Der Hintergrund besteht aus Boden, Grass, Wasser, Bäumen und Wänden.  
Begehbar sind nur Boden und Grass. Die Spielfigur beginnt ganz links, im mittleren Level wartet ein Gegner (Beast), und am rechten Ende der Spielwelt wartet Ganon auf die Spielfigur.    

# Steuerung
Pfeiltaste links bewegt die Spielfigur nach links  
Pfeiltaste rechts bewegt die Spielfigur nach rechts  
Pfeiltaste oben beweget die Spielfigur nach oben  
Pfeilstaste unten bewegt die Spielfigur nach unten  
STRG links verwandelt die Spielfigur in einen Wolf
Shift links verwandelt die Spielfigur zurück  
Leertaste führt einen Schwerthieb aus (Falls das Schwert und Schild aufgehoben wurden)

# Eingebunden Bibliotheken
_pygame_ Hauptbibliothek zur Erstellung des Spiels  
_os_ Zum Abspielen der Musikdatei  
_enum_ wollte ich mal ausprobieren, hat sich angeboten  
menu.py und game.py aus dem Internet geladen   

# Selbst erstellte Klassen da Projektorientierung
Player: Erstellt die Hauptfigur, enthält Methoden für die Bewegung, Spritesund Kollisionskontrolle der Spielerfigur  

Sword: Erstellt ein Schwert im ersten Level  

Shield: Erstellt einen Schild im ersten Level  

Bow: Erstellt einen Bogen im ersten Level  

Ganon: Erstellt den Gegner Ganon in Level 3

Beast: Erstellt den Gegner Beast in Level 2  

Level: Zuständig für den Levelwechsel  

Spielkachel: Erstellt die unsichtbaren Rechtecke der Map für die Kollisionskontrolle des Wassers und der Wände  

Map: Zeichnet die Levels und enthält Methoden zur Erstellung einer Liste der Levelrechtecke  











