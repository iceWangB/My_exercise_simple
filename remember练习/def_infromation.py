# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:05:54 2025

@author: 10981
"""
import json
from pathlib import Path

def infromation_read(paths):
    path=Path(paths)
    if path.exists():
        contents=path.read_text()
        translates=json.loads(contents)
        user_now=input(f"Are your name is {translates['name']}? Y/N ").upper()
        if user_now!='N' and user_now!='Y':
            print("Input really chat！")
        elif user_now=='N':
            infromation_load(path)
        else:
            print(
            f"I remamber you!Your name is {translates['name']}" 
            +f"、sex is {translates['sex']} and city is {translates['city']}")
        return True
    else:
        return False
        
def infromation_load(paths):
    path=Path(paths)
    print("我还不知道你的信息！")
    names=input("请问你的姓名是:")
    sex=input("请问你的性别是:")
    city=input("请问你所在的城市是:")
    infromations={"name":names,"sex":sex,"city":city}
    translates=json.dumps(infromations)
    path.write_text(translates)
    print("I remember for you")    
    

    