#csv (comma separated values) file handling in python
# import csv
# with open("C:\\Users\\ayesh\\Downloads\\Sample-Data.csv","w") as file:
#     file.write("I want to create an AI Model")

# with open("C:\\Users\\ayesh\\Downloads\\Sample-Data.csv","a") as file:
#     file.write("Ayesha Ijaz-Python developer\n")

# f=open("C:\\Users\\ayesh\\Downloads\\Sample-Data1.csv","r") 
# Data=f.readlines()
# c=Data[5]
# # print(c)

# f=open("C:\\Users\\ayesh\\Downloads\\Sample-Data1.csv","r") 
# c=Data[6].split(c.row[","])
# D=c.col[6]
# print(D)


# Task 4: Create CSV from User Input
# Theory: This task teaches how to store structured table data using CSV format. Students must write header first, then records using loop.
# Task: Ask number of students, save name and marks in result.csv with header.



# Task 5: Read CSV and Display Properly
# Theory: Students will read structured CSV data and format output neatly using loop.
# Task: Read result.csv and display as: Name: Ali Marks: 80



# Hands-On Practice Tasks
# Task 1: Create a CSV file 'products.csv' with Product and Price columns. Take input from user.  (CORRECT)
# import csv
# with open("product.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Product", "Price"])
#     product_name = input("Enter Product: ")
#     price = input("Enter Price: ")    
#     writer.writerow([product_name, price])    
#     print("File created and data written successfully!")
    
# Task 2: Create 'marks.csv' and calculate total marks of all students.  (CORRECT)
# import csv
# with open("marks.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Students name", "Marks"])
#     total_marks=0
#     for i in range(5):
#         i+=1
#         student_name = input("Student name: ")
#         marks = int(input("Enter marks: "))
#         total_marks += marks 
    # print("File created and total marks of all students are",total_marks)

# Task 3: Find the student with highest marks from CSV file.
import csv
with open("student_record.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["Students name","Marks"])
    for i in range(1,10):5
    i+=1
    highest_marks=[i]
    if i>highest_marks:
            print("Student name",highest_marks)


# Task 4: Append a new student record using 'a' mode.  (CORRECT-how to jump in next row or column???)
# with open("C:\\Users\\ayesh\\Downloads\\Sample-Data1.csv","a",newline="") as file:
#     file.write("Ayesha Ijaz, Rana Ijaz Hussain, 23, Lahore,28/03/2002\n")
#     print("Student Record Updated")


# Task 5: Create a Pass/Fail system (Marks >= 50 → Pass, else Fail).
# import csv
# with open("Pass_Fail.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Students name", "Marks","Pass","Fail"])
#     for i in range(3):
#         i+=1
#         student_name=input("Student Name:")
#         marks=int(input("Marks:"))
#         if marks>=50:
#             status="Pass"
#             print("Congrtulations PASS")
#         else:
#             status="Fail"
#             print("FAIL!Better Luck Next Time")    
    # writer.writerow([student_name, marks])