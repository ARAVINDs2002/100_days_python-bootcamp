# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tX0zr8hyH8OjY4HzQOhk_axNx8n1v0ru
"""

# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input())
# 🚨 Don't change the code above 👆
bmi=int(weight//(height**2))
# Write your code below this line 👇
print(bmi)