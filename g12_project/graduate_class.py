# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:09:19 2026

@author: vasco
"""
class Graduate:
    def __init__(self, graduate_id, university_id, observations):
        self._graduate_id = graduate_id
        self._university_id = university_id
        self.observations = observations

    @property
    def graduate_id(self):
        return self._graduate_id

    @property
    def university_id(self):
        return self._university_id

    def __str__(self):
        return f"Graduate(ID: {self._graduate_id}, Univ ID: {self._university_id}, Obs: {self.observations})"
