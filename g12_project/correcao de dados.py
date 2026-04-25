# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:10:10 2026

@author: vasco
"""

import sqlite3
import csv

def importar_graduados(ficheiro_csv, db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # 1. Usamos latin-1 para evitar o erro de 'utf-8'
    with open(ficheiro_csv, mode='r', encoding='latin-1') as f:
        # 2. ADICIONADO: delimiter=';' porque o Excel em PT usa ponto e vírgula
        reader = csv.reader(f, delimiter=';') 
        
        try:
            header = next(reader) # Salta o cabeçalho
        except StopIteration:
            print("O ficheiro CSV está vazio!")
            return

        # 3. Limpa a tabela antes de começar para não somar lixo aos novos dados
        cursor.execute("DELETE FROM Graduate")
        
        for i, row in enumerate(reader):
            # Verificação de segurança: a linha tem mesmo as 3 colunas?
            if len(row) >= 3:
                cursor.execute("""
                    INSERT OR IGNORE INTO Graduate (graduate_id, university_id, obs)
                    VALUES (?, ?, ?)
                """, (row[0], row[1], row[2]))
            else:
                print(f"Aviso: Linha {i+2} ignorada por falta de colunas: {row}")

    conn.commit()
    conn.close()
    print("Importação concluída com sucesso e tabela limpa!")

# Para executar:
importar_graduados('g12_Universities_Alumni.csv', 'universidades_alumni.db')