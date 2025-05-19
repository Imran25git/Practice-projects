# -*- coding: utf-8 -*-
# Basic Password Generator Code in python
import random
input("Enter your name: ")
lp = ["ksja?#@!?//1234.","sdasd>>>/987&&^%","asd231kjsa>>><<5<.,-=_+/##@","DHAK_+_+*#@"]
qp = input("You want to Enter or Generate password?").lower()
if qp == "Enter".lower():
  input("Enter your password: ")
elif qp == "Generate".lower():
  print("Generating.... please wait>>>: ")
  print(random.choice(lp))
elif qp != "Enter" or "Generate":
  print("Error")
