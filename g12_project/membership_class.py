# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:08:07 2026

@author: vasco
"""

# -*- coding: utf-8 -*-
from Gclass import Gclass

class Membership(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    # Os atributos devem corresponder exatamente às colunas do dataframe/base de dados
    att = ['university_id', 'association_id', 'registration_date', 'fee']

    def __init__(self, university_id, association_id, registration_date, fee):
        super().__init__()
        self.university_id = university_id
        self.association_id = association_id
        self.registration_date = registration_date
        self.fee = fee

        # Criar uma chave composta (ex: '180_156') para identificar unicamente a inscrição no dicionário
        code = f"{str(self.university_id)}_{str(self.association_id)}"

        Membership.obj[code] = self
        Membership.lst.append(code)