# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:45:44 2025

@author: 10981
"""

class Employee:
    def __init__(self,first_name,last_name,Annual_salary):
        self.first_name=first_name
        self.last_name=last_name
        self.Annual_salary=Annual_salary
    def give_raise(self,add_num=1000):
        self.Annual_salary+=add_num