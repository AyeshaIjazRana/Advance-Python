# loops(for(attendance,temp),while(for pwd)),no concept of do while loop in python
'''a=["aLi","talha","anjum"]
for i in a:
    print("hello",i)
    i+=i
    '''
# for i in range(1,10):
#     tab=5*i
#     print(tab) 
# Temperature Example
# temp=["34 degrees","45 degrees","17 degrees","20 degrees","25 degrees"]
# days=["Monday=","Tuesday=","Wednesday=","Thursday=","Friday="]
# for i, j in zip(days,temp):
#     print (i,j)
#     i+=i
#     j+=j

# temp=["34 degrees","45 degrees","17 degrees","20 degrees","5 degrees"]
# days=["Monday=","Tuesday=","Wednesday=","Thursday=","Friday="]
# # for i in temp:
# #     if days[1]==1:
# #         print(i)

# for i in range(len(days)):
#     for j in range(len(temp)):
#         if i == j: # Only print when the index is the same
#             print(days[i], temp[j])

# a="Ayesha"
# print(len(a))

# TEST (Conditional statements)
# Q6. Write a program to check a person's login system (CORRECT)
# username=input("Enter Username:")
# password=int(input("Enter Password:"))
# if username=="admin":
#     if password==1234:
#      print("Login Successful")
#     else:
#      print("Incorrect Password")
# else:
#     print("Invalid Username") 
# Q5. Write a program to check if a number is greater than 10 (CORRECT)
# num=int(input("Enter a Number="))
# if num>10:
#     print("Number is greater than 10")
#     if num<20:
#         print("Number is less than 20")
#     else:
#         print("Number is not less than 20")
# else:
#     print("Number is not greater than 10")            

# Q4. Write a program to check age category (CORRECT)
# age=int(input("Enter your age:"))
# if age>=13 and age<18:
#     print("You are Teen or Adult")
# elif age>=18:
#      print("You are an Adult")
# else:
#     print("You are a child")   

#Q3. Write a program to check if a number is even (CORRECT)
num=int(input("Enter Number="))
if num%2==0:
    print("Number is Even")
    if num%4==0:
        print("Number is divisible by 4")
    else:
        print("Number is not divisible by 4")
else:
    print("Number is Odd")     


#Q2. Write a program to check if student passed an exam (CORRECT)
# marks=int(input("Enter Student Marks="))
# if marks>=40 and marks<80:
#     print("Passed")
# elif marks>=80:
#      print("Passed with Distinction") 
# else:
#     print("Failed")   
 
# Q1. Write a program to check if a number is positive. If it is positive, check whether it is greater than 50 or not. (CORRECT)
# num=int(input("Enter number:"))
# if num>0:
#    print("Number is positive")
#    if num>50:
#       print("Number is greater than 50")
#    else:
#       print("Number is not greater than 50")
# else:
#    print("Number is Negative")         
 