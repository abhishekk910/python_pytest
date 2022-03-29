from webbrowser import get
import pytest 

def get_age(age):
    assert age > 0, "Age cannot be a negative number"
    print("Age is :", age)

get_age(-10)
get_age(-2) 