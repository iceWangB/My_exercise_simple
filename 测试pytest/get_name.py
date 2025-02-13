# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:40:07 2025

@author: 10981
"""

import functions
# print("输入q退出！")
# while True:
#     first_name=input("姓为：")
#     if first_name=='q':
#         break
#     last_name=input("名为：")
#     if last_name=='q':
#         break
#     full_name=functions.FullName(first_name, last_name)
#     print(f"全名为：{full_name}")

#该测试用例测试上面的内容的FullName方法的是否正确
# def test_fullname():
#     fullname=functions.FullName("alina", "bob")
#     assert fullname=="Alina Bob"


#测试类用例(一次一次运行修改的debug测试)
'''assert(断定)将可以使用多种断定方式，
任何条件语句都可以使用，eg. xxx in xxxs , a != b...等 '''
# from functions import Questionnaire
# question="what's you name?"
# questionaire=Questionnaire(question)
# print("Input q at any time quit!")
# while True:
#     questionaire.show_question()
#     answer=input("name:")
#     questionaire.store_answers(answer)


#测试类用例(使用pytest测试）
# from functions import Questionnaire
# def test_Questionnaire_store_alone():
#     #单个答案测试
#     question="what's you name?"
#     questionnaire=Questionnaire(question)
#     Answers=["aaaaaaa"]
#     questionnaire.store_answers(Answers[0])
#     assert Answers[0] in questionnaire.answers
    
# def test_Questionnaire_store_complex():
#     #多个答案测试    
#     question="what's you name?"
#     questionnaire=Questionnaire(question)
#     Answers=["aaaaaaa","bbbbbbbb","cccccccc"]
#     for answer in Answers:
#         questionnaire.store_answers(answer)
#     for answer in Answers:
#         assert answer in questionnaire.answers
    
    
#测试类用例(使用pytest中的夹具测试，该测试能够将一部分相同重复书写的部分写一次就可以)
from functions import Questionnaire
import pytest
'''该夹具会将标签下的一个函数绑定 在测试（test_开头）函数中传入绑定函数的函数名
将会在测试函数运行时先运行绑定函数并将绑定函数的返回值返回至测试函数中'''
@pytest.fixture #使用夹具必须的标签
def QuestionSurvey():
    question="what's you name?"
    questionnaire=Questionnaire(question)
    return questionnaire

def test_Questionnaire_store_alone(QuestionSurvey):
    answers=["aaaaaaaa"]
    QuestionSurvey.store_answers(answers[0])
    assert answers[0] in QuestionSurvey.answers

def test_Questionnaire_store_complex(QuestionSurvey):
    answers=["aaaaaaa","bbbbbbbb","cccccccc"]
    for answer in answers:
        QuestionSurvey.store_answers(answer)
    for answer in answers:
        assert answer in QuestionSurvey.answers
    
    
    
    
    
    
    
    