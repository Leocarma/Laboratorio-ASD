import pandas as pd
import matplotlib.pyplot as plt

def generate_plots():
    try:
        df = pd.read_csv('risultati.csv')
    except FileNotFoundError:
        print("Il file risultati.csv non è stato trovato. Esegui prima test_abr.py")
        return

    # Usiamo TUTTE E QUATTRO le percentuali generate nel test
    percentages = [0.1, 0.3, 0.5, 0.8]
    trees = df['Tree'].unique()

    # 1. Grafico Tempi di Inserimento (Griglia 2x2)
    plt.figure(figsize=(14, 10))
    for i, pct in enumerate(percentages, 1):
        plt.subplot(2, 2, i)
        df_pct = df[df['DupPct'] == pct]
        for tree in trees:
            subset = df_pct[df_pct['Tree'] == tree]
            plt.plot(subset['Size'], subset['InsertTime'], marker='o', label=tree)
        plt.title(f'Inserimento ({int(pct*100)}% duplicati)')
        plt.xlabel('Numero Totale Dati')
        plt.ylabel('Tempo (secondi)')
        plt.legend()
        plt.grid(True)
    plt.tight_layout()
    plt.savefig('tempi_inserimento_multi.png', dpi=300)
    plt.close()

    # 2. Grafico Tempi di Ricerca (Griglia 2x2)
    plt.figure(figsize=(14, 10))
    for i, pct in enumerate(percentages, 1):
        plt.subplot(2, 2, i)
        df_pct = df[df['DupPct'] == pct]
        for tree in trees:
            subset = df_pct[df_pct['Tree'] == tree]
            plt.plot(subset['Size'], subset['SearchTime'], marker='s', label=tree)
        plt.title(f'Ricerca Mista ({int(pct*100)}% duplicati)')
        plt.xlabel('Numero Totale Dati')
        plt.ylabel('Tempo (secondi)')
        plt.legend()
        plt.grid(True)
    plt.tight_layout()
    plt.savefig('tempi_ricerca_multi.png', dpi=300)
    plt.close()

    # 3. Grafico Altezza Albero (Griglia 2x2)
    plt.figure(figsize=(14, 10))
    for i, pct in enumerate(percentages, 1):
        plt.subplot(2, 2, i)
        df_pct = df[df['DupPct'] == pct]
        for tree in trees:
            subset = df_pct[df_pct['Tree'] == tree]
            plt.plot(subset['Size'], subset['Height'], marker='^', label=tree)
        plt.title(f'Altezza Albero ({int(pct*100)}% duplicati)')
        plt.xlabel('Numero Totale Dati')
        plt.ylabel('Altezza (Numero di salti)')
        plt.legend()
        plt.grid(True)
    plt.tight_layout()
    plt.savefig('altezza_multi.png', dpi=300)
    plt.close()

    print("Grafici 2x2 generati con tutte le percentuali (10%, 30%, 50%, 80%):")
    print("- tempi_inserimento_multi.png")
    print("- tempi_ricerca_multi.png")
    print("- altezza_multi.png")

if __name__ == '__main__':
    generate_plots()
