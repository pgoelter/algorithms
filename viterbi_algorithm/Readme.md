# Übung 3 - Bioinformatik

## Files und Ordner
````
viterbi_algorithm
|
|----main.py             // Einstiegspunkt. Implementierung des parsing der Konsolenargumente und Aufruf der Algorithmen.
|
|----tests.py            // Enthält rudimentäre tests gemäß der Aufgabenstellung (z.B.vergleich reversed sequence)
|
|----viterbi
|       |
|       |---algorithm.py // Enthält die Algorithmen für viterbi und posteriori decoding (Vorwärts- und Rückwärtssuche)
|       |---utils.py     // Helper Funktionen
|
|----wuerfel2021.txt     // Sample Daten.
|----Readme.md        // What you see right now!
|----environment.yml  // Alle dependencies in Form eines .yml files, mit welchem direkt ein Anaconda environment erstellt werden kann.
````
### Installation

1. Die Installation erfordert eine bestehende Anaconda Installation. Hierzu kann entweder Anaconda oder alternativ Miniconda verwendet werden um die virtuelle Umgebung zu erstellen.  
Anaconda Link: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html  
Miniconda Link: https://docs.conda.io/en/latest/miniconda.html
   

2. Mithilfe des im Projektverzeichnis liegenden file **environment.yml** kann die Umgebung erstellt werden. Dazu in einer Konsole (z.B. Anaconda Prompt) in das Projektverzeichnis wechseln und dort den folgenden Befehl ausführen:
    ````bash
    conda env export > environment.yml
    ````  

3. Nach erfolgreicher Installation wurde die Umgebung mit Namen **bioinfo** installiert. Diese kann nun mit folgendem Befehl aktiviert werden:
    ````bash
    conda activate bioinfo
    ````
4. Installation abgeschlossen.

### Ausführen via IDE oder Konsole
Um das Tool auszuführen wird vorausgesetzt, dass die im Installationsschritt aufgeführte virtuelle Umgebung installiert wurde.  

#### Konsole
1. Umgebung aktivieren: 
    ````bash
    conda activate bioinfo
    ````
2. Ins Projektverzeichnis wechseln (../assembly_with_nx/)
3. Tool über Konsolenbefehl starten:
    ````bash
    python main.py "Pfad/zu/.txt/Datei"
    ````
4. Die Ausgabe erfolgt über die Konsole.
5. Für weitere Optionen kann die Hilfe aufgerufen werden:
    ````bash
    python main.py --help
    ````
   
   
#### IDE
1. Anaconda Umgebung in IDE einbinden (z.B. Pycharm)
2. Eintrittspunkt ist **viterbi_algorithm/main.py**
3. Dort können entsprechend Pfad zur Datei, etc.. zum Ausprobieren auch von Hand eingetragen werden.

#### Starten mit der vorgefertigten .exe
Im Projektverzeichnis liegt ein eigenständiges executable (**main.exe**). Diese Datei kann analog wie im Schritt **Konsole** beschrieben über eine beliebige Konsole genutzt werden.  
**Hiermit kann das Tool auch ohne vorige Installation der virtuellen Umgebung ausgeführt werden.**
````bash
main.exe "data/wuerfel2021.txt"
````

**Mit einem weiterem Befehl kann die Input Sequenz umgedreht werden:**
````bash
main.exe --reverse "data/wuerfel2021.txt"
````

**Mit den folgenden Befehlen kann bestimmt werden welche Skala genutzt werden kann (Logarithmiert oder Normal, oder beides):**
````bash
main.exe --scale_both "data/wuerfel2021.txt"

main.exe --scale_log "data/wuerfel2021.txt"

main.exe --scale_norm "data/wuerfel2021.txt"  //Hier kann --scale_norm ausgelassen werden, da es der default Wert ist.
````

** Alle mit der .exe Datei ausgeführten Befehle können analog auch mit python ausgeführt werden indem 'main.exe' durch 'python main.py' ersetzt wird.
#### Verfügbare Optionen
````bash
usage: main.py [-h] [--scale_both] [--scale_log] [--scale_norm] [--reverse] path

Calculate viterbi path from a given file

positional arguments:
  path          The path of the file containing just a dice number sequence

optional arguments:
  -h, --help    show this help message and exit
  --scale_both  Print path with logarithmic and normal scale.
  --scale_log   Print path with logarithmic scale.
  --scale_norm  Print path with normal scale.
  --reverse     Reverses the input the sequence.````
````
## Aufgabe 1 - Viterbi Algorithmus

### Gibt es einen Unterschied je nachdem die normale oder logarithmische Skala verwendet wurde?
Nach Ausführen des Experimentes ist kein Unterschied festzustellen. Der Unterschied macht sich vermutlich erst bei **sehr langen** Sequenzen bemerkbar, da die Zahlen durch die Multiplikation immer kleiner werden.

### Welches Ergebnis würde man vermuten, wenn die Sequenz umgedreht wird?
Beim Umdrehen der Sequenz ergibt sich derselbe Pfad nur umgedreht.

## Aufgabe 2 - Posteriori Dekodierung
Anmerkung: Nur Implementierung der Rückwärtssuche und Vorwärtssuche. Die vollständige Posteriori Implementierung konnte ich leider nicht abschließen.

### Umdrehen der Sequenz und verwenden beider Skalen
Logarithmieren ist bei der Posteriori Dekodierung nicht möglich, da hier eine Summe gebildet wird.

**Experiment konnte nicht durchgeführt werden, da die Ich die Implementierung nicht beenden konnte.**

### Unterschiede zwischen Viterbi und Posteriori-Decodierung
Die **posteriori Dekodierung** liefert den wahrscheinlichsten versteckten Zustand zu einem beliebigen Zeitpunkt im Kontext einer Sequenz von beobachtbaren Zuständen die aus diesen versteckten Zuständen entstanden sind.  

Der **Viterbi-Algorithmus** liefert optimalen Pfad, also eine Abfolge von versteckten Zuständen im Kontext einer Sequenz von beobachtbaren Zuständen die aus diesen versteckten Zuständen entstanden sind.

### Einsatzgebiete
Generell liegen die Einsatzgebiete beider Algorithmen immer dort wo ein Problem durch den ein HMM modelliert werden kann. Also wenn es eine Reihe von versteckten Zuständen gibt und man eine Sequenz von beobachtbaren Zuständen vorliegen hat.
Das sind unter anderem die folgenden Bereiche:  
- Spracherkennung
- Bioinformatik (Mustererkennung)
- Analyse von Zeitreihen
- Gestenerkennung
