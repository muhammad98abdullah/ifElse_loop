num = int(input("Enter your number"));
if num > 0:
    print("This is positive number")
elif num < 0:
    print("This is negative number")
else:
    print("This is zero number")

#================================

age = int(input("Please enter your age"))
if age < 15:
    print("he is minor")
elif age <40:
    print("He is adult")
else:
    print("He is senior citizen")



#=============================

year = int(input("Enter year to check it leap year on not :"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("Not a leap year")



#===============================

even_odd = int(input("Enter number to check it even or odd"))
if even_odd % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")


#=========================
number = int(input("Please enter number to find grade"))
if number >= 80:
    print("Your grade is A+")
elif number >= 70:
    print("Your grade is A")
elif number >= 60:
    print("Your grade is B")
elif number >= 50:
    print("Your grade is C")
elif number >= 40:
    print("Your grade is D")
elif number >= 33:
    print("Your grade is E")
else:
    print("Your grafe is F")




# #==========================
num1 = int(input("Enter number :"))
num2 = int(input("Enter 2nd number:"))
if num1 > num2 :
    print("First number is greater")
else:
    print("Second number is greater")




# #========================
num1 = int(input("Enter number :"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Please enter 3rd number :"))
if num1> num2 and num1 > num3:
    print("First number is grater")
elif num2 > num1 and num2 > num3:
    print("Second number is greater")
else:
    print("Third number is greater")



#===================================
word = input("please enter word to check plandrom or not :")
if word == word[::-1]:
    print("This is plandrom")
else:
    print("This is not a plandrom")






#==================================
a= input("Please enter 1st side")
b= input("Please enter 2nd side")
c= input("Please enter 3rd side")
if a + b > c or a + c > b or b + c >a :
    print("This is a valid triangle")
else:
    print("This is not a valid triangle") 


#=====================
alpha = input("Please enter any alpha bhat to check it vowels or not :")
if alpha in 'aeiouAEIOU':
    print("This word is vowels")
else:
    print("This alphabhat is consonent")



# #==============================
num = int(input("Please enter any number"))
# for i in range(0,num):
if num % 3 == 0 and num % 5 == 0:
        print("This number is multiple to 3 and 5") 
else:
        print("This number is not multiple to 3 and 5")



# #============================
num1= int(input("Please enter first number"))
num2= int(input("Please enter second number"))
opera = input("enter operator")
if opera == '+':
        print(num1 + num2)
elif opera == '-':
        print(num1 - num2)
elif opera == '*':
        print(num1 * num2)
elif opera == '/':
        print(num1 / num2)
else:
        print("Invalid operator")








# #==============================
a = int(input("please enter any number :"))
lower_range = 0
high_range = 1000
if a > lower_range and a < high_range:
        print("This number is in range")
else:
        print("This number is not in range")




#===================
num1 = int(input("Please enter first number:"))
num2 = int(input("Please enter second number:"))
num3 = int(input("Please enter third number:"))
if num1 == num2 == num3:
        print("This is equilateral")
elif num1 == num2 !=num3 or num1 == num3 !=num2 or num2 == num3 != num1:
        print("This is isocales triangle")
else:
        print("This is scalene triangle")




# #==========================================
num1 = int(input("Plz enter first number :"))
if num1 % 2 == 0 and num1 % 3 == 0:
        print("This is required number")
else:
        print("This is not a required number")





#=============================================
U_a = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q.R,S,T,U,V,W,X,Y,Z'
# L_a = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
user = input("Plz enter input:")
if user.isupper():
        print("This is uppercase")
elif user.islower():
        print("This is lower case")
else:
        print("This is mix letter")



#===============================
user = int(input("Please enter value"))
if user == 1:
        print("This is not a prime number")
if user > 1:
        for i in range(2,user):
                if user  % i == 0:
                        print("This is not a prime number")
                        break
        else:
                print("This is prime number")




