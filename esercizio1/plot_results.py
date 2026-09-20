import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

TREE_LABELS = {
    'ABRNormal': 'ABR (Normale)',
    'ABRFlag': 'ABR (Flag)',
    'ABRList': 'ABR (Liste)'
}

COLORS = {
    'ABRNormal': '#1f77b4',
    'ABRFlag':   '#ff7f0e',
    'ABRList':   '#2ca02c'
}

def generate_plots():
    csv_path = os.path.join('risultati', 'risultati.csv')
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Il file {csv_path} non è stato trovato. Esegui prima main.py")
        return

    percentages = [0.1, 0.5, 0.8]
    tree_names = list(TREE_LABELS.keys())
    sizes = sorted(df['Size'].unique())

    if not os.path.exists('risultati'):
        os.makedirs('risultati')

    def create_1x3_bar_plot(y_column, title, y_label, filename, multiplier=1):
        figure, axes = plt.subplots(1, 3, figsize=(21, 6))

        global_max = 0
        for pct in percentages:
            df_pct = df[df['DupPct'] == pct]
            for tree in tree_names:
                subset = df_pct[df_pct['Tree'] == tree]
                vals = subset[y_column].values * multiplier
                if len(vals) > 0:
                    global_max = max(global_max, vals.max())

        y_limit = global_max * 1.10

        for axis, pct in zip(axes, percentages):
            x = np.arange(len(sizes))
            bar_width = 0.25
            df_pct = df[df['DupPct'] == pct]

            for i, tree in enumerate(tree_names):
                subset = df_pct[df_pct['Tree'] == tree].sort_values('Size')
                y_vals = subset[y_column].values * multiplier
                offset = (i - 1) * bar_width
                axis.bar(x + offset, y_vals, bar_width,
                         label=TREE_LABELS[tree],
                         color=COLORS[tree],
                         alpha=0.85,
                         edgecolor='white',
                         linewidth=0.5)

            axis.set_title(f"Duplicati: {int(pct*100)}%", fontsize=14, fontweight='bold')
            axis.set_xlabel("Numero di nodi", fontsize=12)
            axis.set_ylabel(y_label, fontsize=12)
            axis.set_xticks(x)
            axis.set_xticklabels([str(s) for s in sizes], fontsize=10)
            axis.tick_params(axis='y', labelsize=10)
            axis.set_ylim(0, y_limit)
            axis.legend(fontsize=10)
            axis.grid(True, axis='y', alpha=0.3)

        figure.suptitle(title, fontsize=16, fontweight='bold')
        figure.tight_layout(rect=[0, 0, 1, 0.95])
        figure.savefig(os.path.join('risultati', filename), dpi=300, bbox_inches="tight")
        plt.close(figure)

    create_1x3_bar_plot('InsertTime', "Tempo di costruzione per percentuale di duplicati",
                        "Tempo (ms)", 'tempi_inserimento.png', 1000)

    create_1x3_bar_plot('SearchSuccessTime', "Tempo di ricerca (con successo)",
                        "Tempo (ms)", 'tempi_ricerca_successo.png', 1000)

    create_1x3_bar_plot('SearchFailureTime', "Tempo di ricerca (con fallimento)",
                        "Tempo (ms)", 'tempi_ricerca_fallimento.png', 1000)

    create_1x3_bar_plot('Height', "Altezza degli alberi per percentuale di duplicati",
                        "Altezza dell'albero", 'altezza.png', 1)

    create_1x3_bar_plot('Nodes', "Conteggio dei Nodi allocati in memoria",
                        "Numero di Nodi fisici", 'nodi.png', 1)

    print("Grafici salvati nella cartella 'risultati':")
    print("  - tempi_inserimento.png")
    print("  - tempi_ricerca_successo.png")
    print("  - tempi_ricerca_fallimento.png")
    print("  - altezza.png")
    print("  - nodi.png")
