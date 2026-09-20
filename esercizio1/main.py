import os
import sys

from benchmark import run_benchmarks

def main() -> None:
    # Crea la cartella "risultati" se non esiste già
    if not os.path.exists('risultati'):
        os.makedirs('risultati')

    print(" FASE 1: Generazione Dati (benchmark.py) ")
    # Avvia la simulazione, testa gli alberi e salva i dati nel file CSV
    run_benchmarks()
    
    print("\n FASE 2: Generazione Grafici (plot_results.py) ")
    # Importa la funzione per disegnare i grafici e la esegue
    from plot_results import generate_plots
    generate_plots()
    
    print("\nEsecuzione completata! Controlla la cartella 'risultati'.")

if __name__ == "__main__":
    main()
