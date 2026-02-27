#input function-by default gives answer in string (don't give the multiple inputs, one varaiable is for one input only)
# grosssalary=int(input("enter gross salary:"))
# taxpercent=int(input("enter tax percent:"))
# taxamount=grosssalary*(taxpercent)//100
# netsalary=grosssalary-taxamount
# print("total tax amount is",taxamount)
# print("net salary is",netsalary)
# num=input("enter number")
# print(num)
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# print("Sum=",num1+num2) 
# School result card
# name=input("enter student name:")
# total_marks=int(input("Enter total marks:"))
# math=float(input("Enter Math marks:")) 
# computer=float(input("Enter Computer marks:")) 
# physics=float(input("Enter Physics marks:")) 
# english=float(input("Enter English marks:")) 
# chemistry=float(input("Enter Chemistry marks:")) 
# obtained_marks=math+computer+physics+english+chemistry
# average=(math+computer+physics+english+chemistry)//5
# percentage=(obtained_marks/total_marks)*100
# print(name)
# print("Average=", average)
# print("Obtained marks=", obtained_marks)
# print("Percnetage=",(percentage))
# Can we restrict the decimal places??? slicing
# differnet "if" statements are for debugging
a = int(input("Student Percentage: "))
if a>=85:
    print("Grade A")
elif a>=75:  # No need for 'and a<85' because the first 'if' already failed
    print("Grade B")
elif a>=50:  # No need for 'and a<75' because the previous 'elif' failed
    print("Grade C")
else:
    print("Failed")