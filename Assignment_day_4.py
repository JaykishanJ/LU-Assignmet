# -*- coding: utf-8 -*-
"""Assignment_day-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/130KAzlw3UQgp4VVSEgflCjewywWz0c8R
"""

n=int(input("Enter the speed of your air craft:-"))
if n<1000:
  print("you are safe to land")
elif n<4500:
  print("Brings the speed to 1000")
elif n<6500:
  print("turn around")
else:
  prrint("Try again later")