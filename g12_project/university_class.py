# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:07:46 2026

@author: Sofia Teixeira
"""
import Gclass
class University(Gclass):
  obj = dict()
  lst = list()
  pos = 0
  sortkey = ''
  att = ['uni_id','uni_name','foundation_date']
  des = ['University Id','University Name', 'Foundation Date']

def __init__(self, uni_id, uni_name, foundation_date):
  super().__init__()
  self._uni_id = int(uni_id)
  self.uni_name = uni_name
  self.foundation_date = foundation_date 

  University.obj[self._uni_id] = self
  University.lst.append(self._uni_id)

@property
def uni_id(self):
  return int(self._uni_id)

@property
def uni_name(self):
  return self.uni_name

@property
def foundation_date(self):
  return self.foundation_date

def __str__(self):
        return f"University(ID: {self._uni_id}, Univ ID: {self.uni_name}, Obs: {self.foundation_date})"



  

