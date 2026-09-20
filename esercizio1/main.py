import os
import sys

from benchmark import run_benchmarks

def main() -> None:
    if not os.path.exists('risultati'):
        os.makedirs('risultati')

    print(" FASE 1: Generazione Dati (benchmark.py) ")
    run_benchmarks()
    
    print("\n FASE 2: Generazione Grafici (plot_results.py) ")
    from plot_results import generate_plots
    generate_plots()
    
    print("\nEsecuzione completata! Controlla la cartella 'risultati'.")

if __name__ == "__main__":
    main()
