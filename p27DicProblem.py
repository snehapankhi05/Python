"""
 Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

"""

dic={'sneha':100,'khush':100,'shreya':23}
name=input("Please enter name")
if name==dic:
    print(name,"'s marks is",dic.get(name))
else:
    print("not found")