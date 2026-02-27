# Loop Questions
# 1.Print Numbers 1 to 10
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i)
#     i+=i

# 2.#Print numbers from 10 to 1 (reverse order)
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in reversed(a):
#     print(i)

# 3.Write a program to print even numbers from 1 to 20.
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in a:
#     if i%2==0:
#         print(i)

#4.Write a program to print odd numbers between 1 and 15. 
# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in a:
#     if i%2!=0:
#         print(i)

# 5.Ask the user to enter their name. Print the name 5 times using a for loop.
# name=input("Enter your name:")
# for i in range(5):
#     print(name)

# 6.Ask the user to enter a number and print its multiplication table (up to 10).
# num=int(input("Enter a number:"))
# for i in range(1,11):
#     tab=num*i
#     print(num,"*",i,"=",tab)   

# 7.Print numbers from 10 to 50 with a step of 5.
# for i in range(10,51,5):
#     print(i)
  
# 8.Print numbers between 1 and 100 that are divisible by both 3 and 5.
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)


# *
# **
# ***
# ****
# *****
# var="*"
# a=[var]
# print("*\n**\n***\n****\n*****")
# for i in range(1,6):
#     print("*" * i)
    
# palindrome-means starting and ending is same and word doesn't change-example is "civic"
# a=9785
# sum=0
# while a>0:
#     num=a%10
#     sum=sum+num
#     a=a//10
#     print(sum)
# make this number reverse homework
a=9785
reverse_a=0
while a>0:
    num=a%10
    reverse_a=(reverse_a*10)+num
    a=a//10
    print(reverse_a)
