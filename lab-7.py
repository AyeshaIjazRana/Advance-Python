# Quizz(Monday-23/2/26)
# Q1.You have three numbers in variables a, b, c. Find the maximum number of them using ifelse. (CORRECT)
# a=input("Enter 1st number:")
# b=input("Enter 2nd number:")
# c=input("Enter 3rd number:")
# if a>b and a>c:
#     print("The maximum number is a=", a)
# elif b>a and b>c:
#     print("The maximum number is b=",b)
# else:
#     print("The maximum number is c=",c)        

# Q2. You have three numbers in variables a, b, c. Find the minimum number of them using ifelse. (CORRECT)
# a=input("Enter 1st number:")
# b=input("Enter 2nd number:")
# c=input("Enter 3rd number:")
# if a<b and a<c:
#     print("The minimum number is a=", a)
# elif b<a and b<c:
#     print("The minimum number is b=",b)
# else:
#     print("The minimum number is c=",c) 

# Q3. Write a program to print the cube of all numbers from 1 to a given number. (CORRECT)
# • Given number: 6
# • Output: 1 8 27 64 125 216
# for i in range(0,6):
#     i+=1
#     print(i*i*i)

# Q4. Write a program to count how many numbers a divisible by 6 between 1 to 100, and print the final count. (CORRECT)
# count=0
# for i in range(1,101):
#     if i%6==0:
#        count+=1
# print("The final count is",count)        

# Q5. Ask the user to enter a number n. Add numbers from 1 to onwards. If the sum becomes greater than n, stop the loop and print: (CORRECT)
# • The final Sum
# • The number where it stopped

# num = int(input("Enter a number n: "))
# sum = 0
# current_num = 1
# while True:
#     sum+=current_num
#     if sum>num:
#         break
#     current_num += 1
# print("Final Sum:", sum)
# print("Stopped at:", current_num)

# Q6. Ask the user to enter 10 values in a variable (one by one) and print every value in the following manner: (CORRECT)
# • Output: 1 5 7 8 3 67 8 5 0 290
# a=int(input("Enter 1st value:"))
# b=int(input("Enter 2nd value:"))
# c=int(input("Enter 3rd value:"))
# d=int(input("Enter 4th value:"))
# e=int(input("Enter 5th value:"))
# f=int(input("Enter 6th value:"))
# g=int(input("Enter 7th value:"))
# f=int(input("Enter 8th value:"))
# h=int(input("Enter 9th value:"))
# i=int(input("Enter 10th value:"))
# values=[]
# values.append(a)
# values.append(b)
# values.append(c)
# values.append(d)
# values.append(e)
# values.append(f)
# values.append(g)
# values.append(h)
# values.append(i)
# print("Output:",values)

# Q7. Ask the user to enter marks of 5 students (one by one). And find the highest marks from them and print it. (CORRECT)
# student_1=input("Enter 1st student marks=")
# student_2=input("Enter 2nd student marks=")
# student_3=input("Enter 3rd student marks=")
# student_4=input("Enter 4th student marks=")
# student_5=input("Enter 5th student marks=")
# if student_1>student_2 and student_1>student_3 and student_1>student_4 and student_1>student_5:
#     print("Student 1 has highest marks which are:",student_1)
# elif student_2>student_1 and student_2>student_3 and student_2>student_4 and student_2>student_5:
#     print("Student 2 has highest marks which are:",student_2)
# elif student_3>student_1 and student_3>student_2 and student_3>student_4 and student_3>student_5:
#     print("Student 3 has highest marks which are:",student_3) 
# elif student_4>student_1 and student_4>student_2 and student_4>student_3 and student_4>student_5:
#     print("Student 4 has highest marks which are:",student_4)
# else:
#     print("Student 5 has highest marks which are:",student_5)

# Q8. Ask the user to enter a number. Then using a loop calculate the following: (CORRECT)
# • Find Sum of even numbers.
# • Find sum of odd numbers.
# num=int(input("Enter a number="))
# sum_even=0
# sum_odd = 0
# for i in range(1, num+1):
#     if i%2==0:
#         sum_even+=i
#     else:
#         sum_odd+=i
# print("Sum of even numbers:", sum_even)
# print("Sum of odd numbers:", sum_odd)

# Q9. Write a program to calculate the sum of even numbers, sum of odd numbers. Then print the difference between the two sums. (CORRECT)
# num=int(input("Enter a number="))
# sum_even=0
# sum_odd = 0
# for i in range(1, num+1):
#     if i%2==0:
#         sum_even+=i
#     else:
#         sum_odd+=i
# print("Sum of even numbers:", sum_even)
# print("Sum of odd numbers:", sum_odd)
# print("Difference between the two sums:", (sum_even-sum_odd))

