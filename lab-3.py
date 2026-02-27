# Conditional statement-electricity bill
# space complexity(how many space will take for a program-loops are space complexity than conditional statement) and time complexity(how many steps will take for a program)
# p1=5.15
# p2=11.50
# p3=31.001
# p4=50.001
# unit=int(input("Enter number of units:"))
# if(unit<=100):
#     print("Total Bill=",unit*p1)
# elif(unit<=200):
#     print("Total Bill=",unit*p2)
# elif(unit<=300):
#     print("Total Bill=",unit*p3)
# elif(unit<=400):
#     print("Total Bill=",unit*p4)    
# else:
#     print("No Bill found")
# Traffic signals
# light=input("Enter light color:")
# if(light== "red"):
#     print("Stop")
# elif(light=="yellow"):
#     print("Ready")
# elif(light=="green"):
#     print("Go")
# else:
#     print("Light is broken")        
# p1=5.15
# p2=11.50
# p3=31.001
# p4=50.001
# p5=60.66
# unit=float(input("Enter number of units:"))
# if(unit<=100):
#     print("Total Bill=",unit*p1)
# elif(unit<=200):
#     print("Total Bill=",unit*p1+(unit-200)*p2)
# elif(unit<=300):
#     print("Total Bill=",unit*p1+(unit*p2)+(unit-300)*p3)
# elif(unit<=400):
#     print("Total Bill=",unit*p1+(unit*p2)+(unit*p3)+(unit-400)*p4)    
# else:
#     print("Total Bill=",unit*p5)
# Area of circle
# import math
# r=int(input("Enter the radius="))
# if r>0:
#     Area= math.pi*r*r
#     print("Area of circle=",Area)
# else:
#     print("Area of circle cannot be zero or negative")
# # Area of rectangle   
# l=int(input("Length="))
# w=int(input("Width="))
# if l>0 and w>0:
#     Area= l*w
#     print("Area of Rectangle=",Area)
# else:
#     print("Area of rectangle cannot be zero or negative")
# Identify triangle
# angle_1=int(input("Enter the value of angle 1="))
# angle_2=int(input("Enter the value of angle 2="))
# angle_3=int(input("Enter the value of angle 3="))
# sum=angle_1+angle_2+angle_3
# if sum==180:    
#     b=int(input("base="))
#     h=int(input("height="))
#     area=(b*h)/2 
#     print("Given figure is a triangle and Area of triangle is",area)
# else:
#     print("Given figure is not a triangle")
# BMI calculation
# w=int(input("Enter weight="))
# h=int(input("Enter height="))
# BMI=w/(h*h)
# if BMI<0.5:
#     print("You are underweight")
# elif BMI>0.5:
#     print("Your weight is normal")
# else:
#     print("Eat healthy")