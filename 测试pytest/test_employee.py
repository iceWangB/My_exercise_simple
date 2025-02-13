# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:57:20 2025

@author: 10981
"""
from employee import Employee
#测试有错的示例
def test_default_give_raise():
    first_name="Wasd"
    last_name="Almsd"
    annual_salary=5000
    employee=Employee(first_name,last_name,annual_salary)
    employee.give_raise("1000") #故意传入错误参数
    assert employee.Annual_salary == 6000
#测试正确的实例
def test_custom_give_raise():
    first_name="Wasd"
    last_name="Almsd"
    annual_salary=5000
    employee=Employee(first_name,last_name,annual_salary)
    employee.give_raise(1000) 
    assert employee.Annual_salary == 6000
#使用夹具的测试实例
import pytest
@pytest.fixture
def employee_example():
    first_name="Wasd"
    last_name="Almsd"
    annual_salary=5000
    employee=Employee(first_name,last_name,annual_salary)
    return employee
def test_default_give_raise_copy(employee_example):
    employee_example.give_raise("1000") #故意传入错误参数
    assert employee_example.Annual_salary == 6000
def test_custom_give_raise_copy(employee_example):
    employee_example.give_raise(1000) 
    assert employee_example.Annual_salary == 6000