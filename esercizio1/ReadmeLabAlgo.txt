Carmannini, Leonardo, 7136659

TESTO DELL'ESERCIZIO

Vogliamo confrontare vari modi per gestire chiavi duplicate in alberi binari di ricerca (ABR):
- normali ABR;
- alberi con flag booleano;
- alberi con liste interne.

Il progetto implementa in Python le tre strutture dati, ne verifica la correttezza 
algoritmica stampando il numero di nodi allocati, e ne confronta l'altezza strutturale, il conteggio 
dei nodi fisici allocati, il tempo di costruzione (inserimento) e il tempo di 
ricerca (misto successi/fallimenti). Gli esperimenti utilizzano array di dimensioni 
crescenti sporcati con percentuali crescenti di duplicati (10%, 30%, 50%, 80%).

ISTRUZIONI PER L'ESECUZIONE

1) Aprire una console Bash e spostarsi nella cartella del progetto.

2) Installare le dipendenze necessarie:

   pip install -r requirements.txt

3) Eseguire l'esperimento completo descritto nella relazione:

   python main.py

4) Al termine vengono salvati nella cartella "risultati" i dati in formato
   CSV e tre grafici in formato PNG.
