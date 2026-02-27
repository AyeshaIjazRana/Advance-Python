# Python Basic librarires (os, math, sys) and file handling (its important for this course)
import os

print(os.getcwd()) #- (get current directory path)
# os.chdir("C:\\Users\\ayesh\\OneDrive\\Desktop\\Advance Python")
# print(os.listdir())
# os.mkdir("Test")
# os.rename("osdirectory","testdirectory")
# print("rename successful")
# os.removedirs("testdirectory")
# print("remove successful")

# # import sys

# import math
# print(int(math.pow(2,3)))

# Hands-On 1: Square Root Program
# import math
# num = int(input("Enter a number: "))
# if num < 0:
#  print("Square root not possible")
# else:
#  result = math.sqrt(num)
#  print("Square root is:", result)
# Explanation: math.sqrt() calculates square root. If condition prevents negative input errors.

# Hands-On 2: Power Table
# import math
# num = int(input("Enter number: "))
# for i in range(1, 6):
#  result = math.pow(num, i)
#  print(num, "^", i, "=", result)
# Explanation: Loop runs 5 times. math.pow() calculates power. 

# Hands-On 3: Show Current Directory
# import os
# current = os.getcwd()
# print("Current Working Directory:", current)
# Explanation: os.getcwd() returns current working directory path.

# Hands-On 4: Create Folder If Not Exists
# import os
# folder = input("Enter folder name: ")
# if os.path.exists(folder):
#  print("Folder already exists")
# else:
#  os.mkdir(folder)
#  print("Folder created successfully")
# Explanation: os.path.exists() checks existence. os.mkdir() creates folder.

# # Hands-On 5: Folder Creator Using Loop
# import os
# num = int(input("How many folders do you want to create? "))
# for i in range(1, num + 1):
#  folder_name = "Folder" + str(i)
#  if os.path.exists(folder_name):
#    print(folder_name, "already exists")
#  else:
#    os.mkdir(folder_name)
#    print(folder_name, "created successfully")
#    print("Task Completed")
# Explanation: Loop creates multiple folders dynamically and checks existence before creating.

# Hands-On 6: Show Python Version
# import sys
# print("Python Version:")
# print(sys.version)
# Explanation: sys.version shows installed Python version.