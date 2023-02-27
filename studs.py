# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:02:24 2023

@author: Mazin
"""

file = open("stud.txt","r")
students = ""
for i in file:
    students += ",s"+i.strip()+"@student.squ.edu.om"
    
print(students)