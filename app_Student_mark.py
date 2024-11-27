# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:58:05 2024

@author: KRISH
"""

import streamlit as sl

sl.title("Student Mark Predictor")

a = sl.text_input("Enter the number of courses:")
b = sl.text_input("Enter the time study:")


sl.balloons()

import pickle 
with open('student_marks.pkl' , 'rb') as file:
    model = pickle.load(file)

if sl.button("Submit"):
    inp = [[a,b]]
    pre = model.predict(inp)
    sl.write('Prediction : ',pre[0])
    
  