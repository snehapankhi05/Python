"""
You are familiar with basics of input/output and many other useful things in Python.
This module is all about conditional statements like if, elif, else; for, while, etc.

In Python, any conditional statement ends with ':'
(proper indentation must be followed while working through loops).

There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate
 if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false
"""

j_input=(input("Please enter John is angry or not(True/False)"))
s_input=(input("Please enter Smith is angry or not(True/False)"))

j_angry = j_input.strip().lower() == "true"
s_angry = s_input.strip().lower() == "true"


def Angry(j_angry,s_angry):
    if ((j_angry and s_angry) or (not j_angry and not s_angry)):
        return True
    else:
        return False

if Angry(j_angry,s_angry):
    print("You are in trouble")

else:
    print("You are not in trouble")



"""
if j_angry==s_angry:
    print("True: You are in trouble")
else:
    print("False:You are not in Trouble")
    """
