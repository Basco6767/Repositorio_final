# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:08:07 2026

@author: vasco
"""

from gclass import Gclass

class Membership(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ""

    path = "universidades_alumni.db"
    
    att = ["_id", "_graduate_id", "_association_id", "_date"]
    des = ["membership_id", "Graduate ID", "Association ID", "Date"]

    def __init__(self, _id, graduate_id, association_id, registration_date):
        super().__init__()
    
        self._id = Membership.get_id(_id)
        self._graduate_id = graduate_id
        self._association_id = association_id
        self._registration_date = registration_date
        
        Membership.obj[self._membership_id] = self
        if self._membership_id not in Membership.lst:
            Membership.lst.append(self._membership_id)

    @property
    def membership_id(self):
        return self._membership_id

    @property
    def graduate_id(self):
        return self._graduate_id

    @property
    def association_id(self):
        return self._association_id
    
    @property
    def date(self):
        return self._date

    def __str__(self):
  
        return f"Membership(ID: {self._membership_id}, Grad: {self._graduate_id}, Assoc: {self._association_id}, Data: {self._date})"