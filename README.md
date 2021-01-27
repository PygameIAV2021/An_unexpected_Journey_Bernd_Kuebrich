# An_unexpected_Journey_Bernd_Kuebrich

# Warum dieses Spiel?
Da ich schon über 15 Jahren ein rießiger Fan von Rollenspiel/Adventures der Marke "Zelda" bin dachte ich mir es ist bestimmt interessant heraus zu finden 
wieviel Arbeit eigentlich dahinter steckt.
Und ich habe festgestellt, der Aufwand ist rießig.

# Das Spiel
Die Hauptfigur hat die Aufgabe, in der Spielwelt verteilte Items zu finden und aufzusammeln und damit den fießen Gegner Ganon zu besiegen.
Die Spielwelt besteht aus 3 verbundenen Levels. Der Hintergrund besteht aus Boden, Grass, Wasser, Bäumen und Wänden.
Begehbar sind nur Boden und Grass. Die Spielfigur beginnt ganz links, und am rechten Ende wartet Ganon auf die Spielfigur.

# Steuerung
Pfeiltaste links bewegt die Spielfigur nach links
Pfeiltaste rechts bewegt die Spielfigur nach rechts
Pfeiltaste oben beweget die Spielfigur nach oben
Pfeilstaste unten bewegt die Spielfigur nach unten

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

Level: Zuständig für den Levelwechsel

Spielkachel: Zeichnet die unsichtbaren Rechtecke der Map für die Kollisionskontrolle des Wassers und der Wände

Map: Zeichnet die Levels und enthält Methoden zur Erstellung einer Liste der Levelrechtecke











