import pandas as pd
import matplotlib.pyplot as plt

def generate_plots():
    try:
        df = pd.read_csv('risultati.csv')
    except FileNotFoundError:
        print("Il file risultati.csv non è stato trovato. Esegui prima test_abr.py")
        return

    # Filtra i dati per dimensione e % di duplicati per i grafici
    # Confronto Tempi di Inserimento (con 50% duplicati)
    df_50 = df[df['DupPct'] == 0.5]
    
    plt.figure(figsize=(12, 5))
    
    # Inserimento
    plt.subplot(1, 2, 1)
    for tree in df_50['Tree'].unique():
        subset = df_50[df_50['Tree'] == tree]
        plt.plot(subset['Size'], subset['InsertTime'], marker='o', label=tree)
    
    plt.title('Tempi di Inserimento (50% duplicati)')
    plt.xlabel('Numero Totale di Inserimenti')
    plt.ylabel('Tempo (s)')
    plt.legend()
    plt.grid(True)
    
    # Ricerca
    plt.subplot(1, 2, 2)
    for tree in df_50['Tree'].unique():
        subset = df_50[df_50['Tree'] == tree]
        plt.plot(subset['Size'], subset['SearchTime'], marker='s', label=tree)
        
    plt.title('Tempi di Ricerca (50% duplicati)')
    plt.xlabel('Dimensione dell\'albero logico')
    plt.ylabel('Tempo (s)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('tempi_50_pct.png')
    plt.close()
    
    # Altezza alberi
    plt.figure(figsize=(8, 5))
    for tree in df_50['Tree'].unique():
        subset = df_50[df_50['Tree'] == tree]
        plt.plot(subset['Size'], subset['Height'], marker='^', label=tree)
        
    plt.title('Altezza dell\'albero (50% duplicati)')
    plt.xlabel('Numero Totale di Inserimenti')
    plt.ylabel('Altezza (h)')
    plt.legend()
    plt.grid(True)
    plt.savefig('altezza_50_pct.png')
    plt.close()

    print("Grafici generati e salvati in formato PNG (tempi_50_pct.png, altezza_50_pct.png).")

if __name__ == '__main__':
    generate_plots()
