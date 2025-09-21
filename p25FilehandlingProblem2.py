"""
Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file

"""
try:
    file1=open('sample.txt','w')
    file1.write("Hello I have wriiten")
    file1.close()

    file1=open('sample.txt','a')
    file1.write("\nI have appended")

    file1=open('sample.txt','r')
    read=file1.read()
    print(read)

except FileNotFoundError:
    print("File not found")