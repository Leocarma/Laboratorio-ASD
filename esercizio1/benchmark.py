import time
import random
import csv
import os
from abr_normal import ABRNormal
from abr_flag import ABRFlag
from abr_list import ABRList

# Le grandezze degli array su cui testeremo gli alberi
DEFAULT_SIZES = (1000, 2000, 3000, 5000, 10000)

def run_benchmarks(sizes=DEFAULT_SIZES):
    # Le diverse percentuali di chiavi duplicate da inserire
    duplicate_percentages = [0.1, 0.3, 0.5, 0.8] # 10%, 30%, 50%, 80% di duplicati
    
    # Lista in cui salveremo i risultati prima di scriverli sul CSV
    results = []

    # Iteriamo per ogni dimensione dell'array
    for size in sizes:
        # Iteriamo per ogni percentuale di duplicati
        for dup_pct in duplicate_percentages:
            # Calcoliamo quanti elementi devono essere univoci
            num_unique = int(size * (1 - dup_pct))
            if num_unique == 0:
                num_unique = 1

            # Generiamo numeri univoci casuali
            unique_keys = random.sample(range(1, size * 10), num_unique)
            data = []
            
            # Aggiungiamo i numeri univoci all'array finale
            data.extend(unique_keys)
            
            # Calcoliamo quanti duplicati servono per raggiungere la size voluta
            num_duplicates = size - len(data)
            for _ in range(num_duplicates):
                # Scegliamo a caso un numero univoco esistente e lo duplichiamo
                data.append(random.choice(unique_keys))
                
            # Mischiamo l'array affinché i duplicati siano sparsi casualmente
            random.shuffle(data)
            
            # Instanziamo i tre alberi da mettere a confronto
            trees = {
                'ABRNormal': ABRNormal(),
                'ABRFlag': ABRFlag(),
                'ABRList': ABRList()
            }
            
            # Avviamo il test per ogni albero
            for tree_name, tree in trees.items():
                
                # TEST 1: TEMPO DI INSERIMENTO
                start_time = time.perf_counter()
                for key in data:
                    tree.insert(key)
                end_time = time.perf_counter()
                insert_time = end_time - start_time

                # Prepariamo un array per il test di ricerca mista:
                # 50% di numeri presi dall'array (successi certi)
                # 50% di numeri esterni al range (fallimenti certi)
                search_keys = data[:size//2] + random.sample(range(size*10, size*20), size//2)
                
                # TEST 2: TEMPO DI RICERCA MISTA
                start_time = time.perf_counter()
                for key in search_keys:
                    tree.search(key)
                end_time = time.perf_counter()
                search_time = end_time - start_time
                
                # Estraiamo le proprietà strutturali per capire come si sono comportati
                altezza = tree.altezza()
                nodi = tree.conta_nodi()
                
                # Salviamo la statistica corrente
                results.append({
                    'Tree': tree_name,
                    'Size': size,
                    'DupPct': dup_pct,
                    'InsertTime': insert_time,
                    'SearchTime': search_time,
                    'Height': altezza,
                    'Nodes': nodi
                })
                
    # Definiamo il percorso di salvataggio
    csv_path = os.path.join('risultati', 'risultati.csv')
    if not os.path.exists('risultati'):
        os.makedirs('risultati')
        
    # Scriviamo tutti i risultati nel file CSV
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Tree', 'Size', 'DupPct', 'InsertTime', 'SearchTime', 'Height', 'Nodes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            writer.writerow(row)
            
    print(f"Test completati su dimensioni {sizes} e risultati salvati in {csv_path}")
    return results

if __name__ == '__main__':
    run_benchmarks()
