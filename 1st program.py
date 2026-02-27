# print("Salam World")
# name="Ayesha" #strings means which are in double commas
# age=23  #assignment operator is = which means assigning the value
# print(name , age)
# print ("my name is:",name)
# age2 = age
# print (age2)
# print(type(name)) #type means data types str, int, float(decimal number), 5 types boolean, none 
# print(type(age))
#print sum
# a=5
# b=3
# sum=a+b
# diff=a-b
# print(diff) #for comment out shortcut key is ctrl+/
# print(sum)
# print(a ** b) #to find the power a^b
# print(a % b) #to find the remainder
#input in python
# name=input("enter your name:")
# print("welcome", name)

# Q1.Write a program to input two numbers and find their sum
# a=int(input("a="))
# b=int(input("b="))
# print("sum=",a+b)

# Q2. input length of square and find its area
# l=int(input("length of square="))
# Area=l*l
# print("Area of square=",Area)

# Q3. Input 3 floating point number and find their average
# firstnumber=float(input("First Number="))
# secondnumber=float(input("Second Number="))
# thirdnumber=float(input("Third Number="))
# Average=(firstnumber+secondnumber+thirdnumber)/3
# print("Average of 3 floating numbers=", Average)

# Q4. Input 2 int numbers, print true if a>=b else False
# a=int(input("a="))
# b=int(input("b="))
# print(a>=b)

# String Indexing-tells the location 

# str="Ayesha"
# print(str[0]) 
# print(len(str))

# string slicing-breakdown string-str[starting ind:ending ind]
# str="Ayesha_Ijaz"
# # print(str[ 7:11])
# print(str[-11:-5])

# WAP to check if a number entered by the user is odd or even
# a=int(input("enter a number:"))
# if(a%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")

# list- mutable data type that can be changeable
# list=["Ayesha",23,99.9,"Lahore"]
# print(len(list))
# print(list[0])
# marks=[85,94,76,56,41]
# print(marks[0:4])
# print(marks[-3:-1])

# list method 
# list=[2,1,3]
# # list.append(4) (this is called mutation means 4 has been added to the list)
# # list.sort() (ascending order)
# # list.sort(reverse=True) (descending order)
# # list.reverse() (reverse the list)
# # list.insert(1,5) (add any element on any index)
# print(list) 

# Tuples- immutable data type
# tup=(2,1,3,1)
# print(tup[1])
# tup=() (Empty tuple)
# print(tup)
# print(type(tup)) (for single value in tuple always end with comma like tup=(1,))

# Q1. WAP to ask the user to enter names of their 3 favorite movies and store them in a list
# mov1=input("Enter your 1 favorite movie:")
# mov2=input("Enter your 2 favorite movie:")
# mov3=input("Enter your 3 favorite movie:")
# movies=[]
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# Q2. WAP to check if a list contains a palindrome(means ma'am, civic,racecar) of elements.
# to find palindrome first copy and then reverse
# list1=[1,2,3,2,1] 
# # list2=[1,"abc","abc",1]
# copy_list1=list1.copy()
# copy_list1.reverse()
# if(copy_list1==list1):
#     print("Palindrome")
# else:
#     print("not palindrome")    

# WAP to count the number of students with the "A" grade in following tuple
# ["C","D","A","A","B","B","A"] and sort in ascending order
# grade=["C","D","A","A","B","B","A"]
# # print(grade.count("A"))
# grade.sort()
# print(grade)

# Lecture 4
# Dictionary in Python-these are used to store data values in key:value pairs
 