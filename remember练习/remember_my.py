# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:33:32 2025

@author: 10981
"""
import def_infromation
from pathlib import Path
path=Path("user_infromation.json")
if def_infromation.infromation_read(path)==False:
    def_infromation.infromation_load(path)



