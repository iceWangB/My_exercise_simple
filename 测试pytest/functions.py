# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:23:13 2025

@author: 10981
"""
def FullName(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()


#类的测试用例 pytest
class Questionnaire:
    #问卷调查类
    def __init__(self,question):
        self.question=question
        self.answers=[]
        
    def show_question(self):
        #展示问题
        print(f"The question is {self.question}")
        
    def store_answers(self,answer):
        #保存答案
        self.answers.append(answer)
        