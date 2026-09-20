import pandas as pd
import matplotlib.pyplot as plt
import os

TREE_LABELS = {
    'ABRNormal': 'ABR (Normale)',
    'ABRFlag': 'ABR (Flag)',
    'ABRList': 'ABR (Liste)'
}

def generate_plots():
    csv_path = os.path.join('risultati', 'risultati.csv')
    try:
        # Carica tutti i dati generati dal file benchmark.py
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Il file {csv_path} non è stato trovato. Esegui prima main.py")
        return

    percentages = [0.1, 0.3, 0.5, 0.8]
    trees = df['Tree'].unique()

    if not os.path.exists('risultati'):
        os.makedirs('risultati')

    # 1. Grafico Tempi di Inserimento
    figure, axes = plt.subplots(1, 4, figsize=(20, 5))
    for axis, pct in zip(axes, percentages):
        # Filtra i dati solo per la percentuale corrente
        df_pct = df[df['DupPct'] == pct]
        for tree in trees:
            subset = df_pct[df_pct['Tree'] == tree]
            # Convertiamo i secondi in millisecondi
            build_ms = subset['InsertTime'] * 1000
            axis.plot(subset['Size'], build_ms, marker="o", label=TREE_LABELS.get(tree, tree))
            
        axis.set_title(f"Duplicati: {int(pct*100)}%")
        axis.set_xlabel("Numero di nodi")
        axis.set_ylabel("Tempo di costruzione (ms)")
        axis.grid(True)
        axis.legend()
    
    # Salva il grafico ad alta risoluzione tagliando i bordi inutili
    figure.suptitle("Tempo di costruzione per percentuale di duplicati")
    figure.tight_layout()
    figure.savefig(os.path.join('risultati', 'tempi_inserimento_multi.png'), dpi=400, bbox_inches="tight")
    plt.close(figure)

    # 2. Grafico Tempi di Ricerca
    figure, axes = plt.subplots(1, 4, figsize=(20, 5))
    for axis, pct in zip(axes, percentages):
        df_pct = df[df['DupPct'] == pct]
        for tree in trees:
            subset = df_pct[df_pct['Tree'] == tree]
            # Convertiamo i secondi in millisecondi
            search_ms = subset['SearchTime'] * 1000
            axis.plot(subset['Size'], search_ms, marker="o", label=TREE_LABELS.get(tree, tree))
            
        axis.set_title(f"Duplicati: {int(pct*100)}%")
        axis.set_xlabel("Numero di nodi")
        axis.set_ylabel("Tempo di ricerca mista (ms)")
        axis.grid(True)
        axis.legend()
        
    figure.suptitle("Tempo di ricerca per percentuale di duplicati")
    figure.tight_layout()
    figure.savefig(os.path.join('risultati', 'tempi_ricerca_multi.png'), dpi=400, bbox_inches="tight")
    plt.close(figure)

    # 3. Grafico Altezza Albero
    figure, axes = plt.subplots(1, 4, figsize=(20, 5))
    for axis, pct in zip(axes, percentages):
        df_pct = df[df['DupPct'] == pct]
        for tree in trees:
            subset = df_pct[df_pct['Tree'] == tree]
            axis.plot(subset['Size'], subset['Height'], marker="o", label=TREE_LABELS.get(tree, tree))
            
        axis.set_title(f"Duplicati: {int(pct*100)}%")
        axis.set_xlabel("Numero di nodi")
        axis.set_ylabel("Altezza dell'albero")
        axis.grid(True)
        axis.legend()
        
    figure.suptitle("Altezza degli alberi per percentuale di duplicati")
    figure.tight_layout()
    figure.savefig(os.path.join('risultati', 'altezza_multi.png'), dpi=400, bbox_inches="tight")
    plt.close(figure)

    print("Grafici 1x4 salvati nella cartella 'risultati':")
    print("- tempi_inserimento_multi.png")
    print("- tempi_ricerca_multi.png")
    print("- altezza_multi.png")
