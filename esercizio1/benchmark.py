import time
import random
import csv
import os
import sys
from abr_normal import ABRNormal
from abr_flag import ABRFlag
from abr_list import ABRList

sys.setrecursionlimit(50000)

DEFAULT_SIZES = (500, 1000, 2000, 3000, 5000, 7500, 10000)

def run_benchmarks(sizes=DEFAULT_SIZES):
    # 3 percentuali: Bassa (10%), Media (50%), Alta (80%)
    duplicate_percentages = [0.1, 0.5, 0.8] 
    
    results = []

    for size in sizes:
        for dup_pct in duplicate_percentages:
            
            accumulated = {
                'ABRNormal': {'InsertTime': 0, 'SearchSuccessTime': 0, 'SearchFailureTime': 0, 'Height': 0, 'Nodes': 0},
                'ABRFlag': {'InsertTime': 0, 'SearchSuccessTime': 0, 'SearchFailureTime': 0, 'Height': 0, 'Nodes': 0},
                'ABRList': {'InsertTime': 0, 'SearchSuccessTime': 0, 'SearchFailureTime': 0, 'Height': 0, 'Nodes': 0}
            }

            repetitions = 40
            
            for _ in range(repetitions):
                
                # 1. Calcoliamo il numero esatto di chiavi univoche necessarie
                num_unique = int(size * (1 - dup_pct))
                if num_unique == 0:
                    num_unique = 1

                # 2. Peschiamo chiavi casuali in un range largo
                unique_keys = random.sample(range(1, size * 10), num_unique)
                
                data = []
                data.extend(unique_keys)
                
                # 3. Riempiamo i posti restanti per raggiungere 'size' inserendo duplicati scelti a caso
                num_duplicates = size - len(data)
                for _ in range(num_duplicates):
                    data.append(random.choice(unique_keys))
                    
                # 4. Mescoliamo per evitare di inserire dati in ordine (caso peggiore ABR)
                random.shuffle(data)
                
                trees = {
                    'ABRNormal': ABRNormal(),
                    'ABRFlag': ABRFlag(),
                    'ABRList': ABRList()
                }
                
                for tree_name, tree in trees.items():
                    # TEST 1: INSERIMENTO
                    start_time = time.perf_counter()
                    for key in data:
                        tree.insert(key)
                    insert_time = time.perf_counter() - start_time

                    # TEST 2: RICERCA CON SUCCESSO
                    search_success_keys = random.choices(unique_keys, k=size)
                    
                    start_time = time.perf_counter()
                    for key in search_success_keys:
                        tree.search(key)
                    search_success_time = time.perf_counter() - start_time
                    
                    # TEST 3: RICERCA CON FALLIMENTO
                    existing_set = set(data)
                    all_possible = range(1, size * 10)
                    non_existing = [k for k in random.sample(all_possible, min(size * 3, len(all_possible))) if k not in existing_set]
                    while len(non_existing) < size:
                        non_existing.append(random.randint(size * 10, size * 12))
                    search_fail_keys = non_existing[:size]
                    
                    start_time = time.perf_counter()
                    for key in search_fail_keys:
                        tree.search(key)
                    search_fail_time = time.perf_counter() - start_time
                    
                    accumulated[tree_name]['InsertTime'] += insert_time
                    accumulated[tree_name]['SearchSuccessTime'] += search_success_time
                    accumulated[tree_name]['SearchFailureTime'] += search_fail_time
                    accumulated[tree_name]['Height'] += tree.altezza()
                    accumulated[tree_name]['Nodes'] += tree.conta_nodi()
            
            for tree_name in accumulated:
                results.append({
                    'Tree': tree_name,
                    'Size': size,
                    'DupPct': dup_pct,
                    'InsertTime': accumulated[tree_name]['InsertTime'] / repetitions,
                    'SearchSuccessTime': accumulated[tree_name]['SearchSuccessTime'] / repetitions,
                    'SearchFailureTime': accumulated[tree_name]['SearchFailureTime'] / repetitions,
                    'Height': accumulated[tree_name]['Height'] / repetitions,
                    'Nodes': accumulated[tree_name]['Nodes'] // repetitions
                })
                
    csv_path = os.path.join('risultati', 'risultati.csv')
    if not os.path.exists('risultati'):
        os.makedirs('risultati')
        
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Tree', 'Size', 'DupPct', 'InsertTime', 'SearchSuccessTime', 'SearchFailureTime', 'Height', 'Nodes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
            
    print(f"Test completati su dimensioni {sizes} e risultati salvati in {csv_path}")
    return results

if __name__ == '__main__':
    run_benchmarks()
