import nbformat as nbf

nb = nbf.v4.new_notebook()

testo_intro = """# Esercizio 2: Confronto algoritmi di ordinamento
In questo notebook metteremo a confronto due noti algoritmi di ordinamento: **Insertion Sort** e **Quick Sort**.

L'obiettivo è misurare le loro prestazioni su array di diverse dimensioni e in diversi stati di ordinamento iniziale:
1. Caso medio: Array con elementi casuali
2. Caso ottimo: Array già ordinati (vantaggioso per Insertion Sort)
3. Caso pessimo: Array ordinati in senso inverso

Al termine verranno generati dei grafici per evidenziare visivamente la complessità computazionale dei due algoritmi.
"""

codice_sort = """def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Wrapper per facilitare la misurazione senza alterare l'array originale
def test_insertion_sort(arr):
    import copy
    arr_copy = copy.deepcopy(arr)
    insertion_sort(arr_copy)
    return arr_copy

def test_quick_sort(arr):
    import copy
    arr_copy = copy.deepcopy(arr)
    return quick_sort(arr_copy)
"""

testo_dati = """## Generazione dei dati di test e Misurazione
Useremo il modulo `time` per la misurazione, eseguendo i test su array randomici di varie dimensioni.
Assicuriamoci di variare la dimensione dell'input per poter graficare le curve di complessità.
"""

codice_test = """import time
import random
import matplotlib.pyplot as plt

dimensioni = [100, 500, 1000, 2000, 5000]

tempi_ins_casuale = []
tempi_quick_casuale = []

tempi_ins_ordinato = []
tempi_quick_ordinato = []

tempi_ins_inverso = []
tempi_quick_inverso = []

for n in dimensioni:
    # 1. Dati casuali
    dati_casuali = [random.randint(1, 10000) for _ in range(n)]
    
    start = time.perf_counter()
    test_insertion_sort(dati_casuali)
    tempi_ins_casuale.append(time.perf_counter() - start)
    
    start = time.perf_counter()
    test_quick_sort(dati_casuali)
    tempi_quick_casuale.append(time.perf_counter() - start)
    
    # 2. Dati ordinati
    dati_ordinati = sorted(dati_casuali)
    
    start = time.perf_counter()
    test_insertion_sort(dati_ordinati)
    tempi_ins_ordinato.append(time.perf_counter() - start)
    
    start = time.perf_counter()
    test_quick_sort(dati_ordinati)
    tempi_quick_ordinato.append(time.perf_counter() - start)
    
    # 3. Dati inversamente ordinati
    dati_inversi = list(reversed(dati_ordinati))
    
    start = time.perf_counter()
    test_insertion_sort(dati_inversi)
    tempi_ins_inverso.append(time.perf_counter() - start)
    
    start = time.perf_counter()
    test_quick_sort(dati_inversi)
    tempi_quick_inverso.append(time.perf_counter() - start)
    
print("Test completati!")
"""

testo_plot = """## Analisi dei Risultati
Generiamo i grafici per capire visivamente le differenze di tempo di esecuzione tra i due algoritmi.
"""

codice_plot = """plt.figure(figsize=(15, 5))

# Grafico caso casuale
plt.subplot(1, 3, 1)
plt.plot(dimensioni, tempi_ins_casuale, label='Insertion Sort', marker='o')
plt.plot(dimensioni, tempi_quick_casuale, label='Quick Sort', marker='s')
plt.title("Caso Medio (Dati casuali)")
plt.xlabel("Dimensione array (N)")
plt.ylabel("Tempo (s)")
plt.legend()
plt.grid(True)

# Grafico caso ordinato
plt.subplot(1, 3, 2)
plt.plot(dimensioni, tempi_ins_ordinato, label='Insertion Sort', marker='o')
plt.plot(dimensioni, tempi_quick_ordinato, label='Quick Sort', marker='s')
plt.title("Caso Ottimo (Dati già ordinati)")
plt.xlabel("Dimensione array (N)")
plt.legend()
plt.grid(True)

# Grafico caso inverso
plt.subplot(1, 3, 3)
plt.plot(dimensioni, tempi_ins_inverso, label='Insertion Sort', marker='o')
plt.plot(dimensioni, tempi_quick_inverso, label='Quick Sort', marker='s')
plt.title("Caso Pessimo (Dati inversamente ordinati)")
plt.xlabel("Dimensione array (N)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
"""

testo_conclusioni = """## Conclusioni
Dai grafici emergono chiaramente le differenze computazionali tra i due algoritmi:
*   **Caso Medio (Casual)**: Quick Sort ha prestazioni nettamente superiori a Insertion Sort. Mentre Insertion Sort ha una complessità temporale di $O(N^2)$, Quick Sort esegue tipicamente in tempo proporzionale a $O(N \log N)$.
*   **Caso Ottimo (Array ordinato)**: Insertion Sort risulta estremamente efficiente e si comporta quasi come un algoritmo lineare $O(N)$ poiché il loop interno si ferma immediatamente (non servono scambi). Quick Sort (senza ottimizzazioni per la scelta del pivot come il "median-of-three") rimane su $O(N \log N)$.
*   **Caso Pessimo (Array inversamente ordinato)**: In questo scenario, l'Insertion Sort deve fare il numero massimo di confronti e scambi per ogni elemento, toccando il suo limite superiore (struttura quadratica chiara). Quick Sort (con l'implementazione in cui il pivot è scelto centralmente) mantiene la sua efficienza $O(N \log N)$. Si noti che se scegliessimo l'ultimo elemento come pivot in un array già ordinato (non è il nostro caso), la complessità di Quick Sort degenererebbe in quadratica.

Nel complesso, Insertion Sort si rivela utile per set di dati molto ridotti o che si presuppone siano "quasi ordinati", ma per quantità di dati più significative la scelta del Quick Sort è ampiamente giustificata.
"""

nb.cells = [
    nbf.v4.new_markdown_cell(testo_intro),
    nbf.v4.new_code_cell(codice_sort),
    nbf.v4.new_markdown_cell(testo_dati),
    nbf.v4.new_code_cell(codice_test),
    nbf.v4.new_markdown_cell(testo_plot),
    nbf.v4.new_code_cell(codice_plot),
    nbf.v4.new_markdown_cell(testo_conclusioni)
]

with open('sorting_comparison.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
print("Notebook creato con successo.")
