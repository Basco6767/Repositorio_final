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

    print("\n--- 2. Teste de Inserção (Membership) ---")
   
    if len(Graduate.lst) > 0 and len(Association.lst) > 0:
     
        g_id = Graduate.lst[0]
        a_id = Association.lst[0]
        
       
        nova_inscricao = Membership(0, g_id, a_id, "2026-04-07")
        
      
        try:
            Membership.insert(nova_inscricao.membership_id)
            print(f"Sucesso: Inscrição gravada na DB: {nova_inscricao}")
        except Exception as e:
            print(f"Erro ao gravar na DB: {e}")
    else:
        print("Aviso: Teste de inserção abortado (Tabelas Graduate ou Association vazias).")

    print("\n--- 3. Lista de Inscrições Ativas (Navegação) ---")
  
    m = Membership.first()
    if not m:
        print("Nenhuma inscrição encontrada.")
    else:
        while m:
           
            print(f"ID Inscrição: {m.membership_id} | Graduado: {m.graduate_id} | Assoc: {m.association_id} | Data: {m.date}")
            m = Membership.nextrec()

    print("\n--- 4. Teste de Procura (Shortcut find) ---")
   
    res = Graduate.find(1, "_university_id")
    print(f"Existem {len(res)} graduados ligados à Universidade ID 1.")

if __name__ == "__main__":
    main()