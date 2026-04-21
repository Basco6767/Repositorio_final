# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:02:29 2026

@author: vasco
"""

from university_class import University
from graduate_class import Graduate
from association_class import Association
from membership_class import Membership

def main():
    db = "universidades_alumni.db"

    print("--- 1. Lendo Base de Dados ---")
    University.read(db)
    Graduate.read(db)
    Association.read(db)
    Membership.read(db)
    
    print(f"Dados em memória: {len(University.lst)} Universidades, {len(Graduate.lst)} Graduados.")

    print("\n--- 2. Lista de Associações (Navegação) ---")
 
    index = Membership.first()
    if index is not None and index < len(Membership.lst):
        m = Membership.lst[index]
        print(f"Uni ID: {m._university_id}")    
    if not m:
        print("Nenhuma inscrição encontrada.")
    else:
        count = 0
        while m and count < 5:
          
            print(f"Uni ID: {m._university_id} | Assoc ID: {m._association_id} | Data: {m._registration_date}")
            
           
            current_id = m._university_id
            m = Membership.next()
            
          
            if m and m._university_id == current_id:
                break
            count += 1

    print("\n--- 3. Teste de Ordenação ---")
    if len(University.lst) > 0:
        University.sort("uni_name") 
        u = University.first()
        print(f"Primeira universidade (A-Z): {u._name}")

if __name__ == "__main__":
    main()