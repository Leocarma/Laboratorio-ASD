Carmannini, Leonardo, 7136659

TESTO DELL'ESERCIZIO

Vogliamo confrontare vari modi per gestire chiavi duplicate in alberi binari di ricerca (ABR):
- normali ABR;
- alberi con flag booleano;
- alberi con liste interne.

Il progetto implementa in Python le tre strutture dati, ne verifica la correttezza 
algoritmica stampando il numero di nodi allocati, e ne confronta l'altezza strutturale, il conteggio 
dei nodi fisici allocati, il tempo di costruzione (inserimento) e il tempo di 
ricerca (suddiviso tra ricerca con successo e fallimento). Gli esperimenti utilizzano array di dimensioni 
crescenti con percentuali variabili di duplicati (10%, 50%, 80%).

ISTRUZIONI PER L'ESECUZIONE

1) Aprire un terminale (es. Anaconda Prompt o PowerShell) e spostarsi nella cartella del progetto.

2) Installare le dipendenze necessarie:

   pip install -r requirements.txt

3) Eseguire l'esperimento completo descritto nella relazione:

   python main.py

4) Al termine, nella cartella "risultati" verranno salvati i dati in formato
   CSV e 5 grafici in formato PNG per il confronto delle metriche.
