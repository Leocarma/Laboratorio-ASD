import time
import random
import csv
from abr_normal import ABRNormal
from abr_flag import ABRFlag
from abr_list import ABRList

def run_tests():
    sizes = [1000, 2000, 3000, 5000, 10000]
    duplicate_percentages = [0.1, 0.3, 0.5, 0.8] # 10%, 30%, 50%, 80% di duplicati
    
    results = []

    for size in sizes:
        for dup_pct in duplicate_percentages:
            # Generiamo prima i dati unici come differenza con la percentuale di duplicati
            # Es: Supponiamo di dover creare 1000 numeri di cui il 30% dup, 700 saranno unici e 300 quelli duplicati
            num_unique = int(size * (1 - dup_pct))
            # Nel caso in cui si producano il 100% di duplicati (cosa che non succede nel nostro caso, ma per buona pratica poniamo comunque il controllo)
            # La lista num_unique sarebbe vuota, logicamente questo è impossibile, in quanto è impossibile creare 1000 fotocopie tutte uguali
            # Senza prima partire dalla fotocopia originale unica
            if num_unique == 0:
                num_unique = 1

            # Pesca delle chiavi uniche
            unique_keys = random.sample(range(1, size * 10), num_unique)
            data = []
            
            # Aggiunge le chiavi uniche
            data.extend(unique_keys)
            
            # Aggiunge i duplicati scegliendo a caso tra le chiavi uniche
            num_duplicates = size - len(data)
            for _ in range(num_duplicates):
                data.append(random.choice(unique_keys))
                
            # Mescola i dati
            random.shuffle(data)
            
            # Test per ogni struttura
            trees = {
                'ABRNormal': ABRNormal(),
                'ABRFlag': ABRFlag(),
                'ABRList': ABRList()
            }
            
            for tree_name, tree in trees.items():
                # Inserimento
                start_time = time.perf_counter()
                for key in data:
                    tree.insert(key)
                end_time = time.perf_counter()
                insert_time = end_time - start_time

                # Ricerca di chiavi esistenti e inesistenti (miste)
                # Vogliamo testare sia ricerce con successo che senza successo, scegliamo un rapporto 50 e 50
                # Prendiamo un 50% di numeri sicuramente dentro all'albero e un'altra metà che non è presente
                search_keys = data[:size//2] + random.sample(range(size*10, size*20), size//2)
                
                start_time = time.perf_counter()
                for key in search_keys:
                    tree.search(key)
                end_time = time.perf_counter()
                search_time = end_time - start_time
                
                # Metriche strutturali
                altezza = tree.altezza()
                nodi = tree.conta_nodi()
                
                results.append({
                    'Tree': tree_name,
                    'Size': size,
                    'DupPct': dup_pct,
                    'InsertTime': insert_time,
                    'SearchTime': search_time,
                    'Height': altezza,
                    'Nodes': nodi
                })
                
    # Salva i risultati
    with open('risultati.csv', 'w', newline='') as csvfile:
        fieldnames = ['Tree', 'Size', 'DupPct', 'InsertTime', 'SearchTime', 'Height', 'Nodes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in results:
            writer.writerow(row)
            
    print("Test completati e risultati salvati in risultati.csv")

if __name__ == '__main__':
    run_tests()
