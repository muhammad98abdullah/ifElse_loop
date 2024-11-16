for i in range(0,20):
    print(i)


#===================================
for i in range(0,10):
    print(i**2)

#==========================
number = 2
while number <= 50:
    print(number)
    number +=2    



# #================
total_sum = 0
for i in range(0,100):
    total_sum += i

print("sum", total_sum)


# #=====================
user = int(input("Please eneter any number to print its table :"))
for i in range(0,11):
    print(user , " * ", i , " = ", user*i)



#=======================
number = 1
while number <=100:
    print(number)

    number +=2



#=======================
st = "Hello world!"
for i in st:
    print(i)



# #===============
user = int(input("Enter number :"))
factorial = 1
i = 1 
while i <= user:
    factorial *= i
    i +=1
print(f"Factorial of {user} is {factorial}")


#==============================
for i in range(10,0,-1):
    print(i)



#=======================
iny = str(505)
digit_count = 0
for digit in iny:
    digit_count +=1


print(f"The number of digits in {iny} is: {digit_count}")


a , b = 0 , 1
for _ in range(10):
    print(a , end=" ")

    a, b = b, a + b    
 

 #=================




user = int(input("Enter any number :"))
user_str = str(user)
rever = reversed(user_str)
for num in rever:
    
    print(num, end="")






#=============================
for i in range(20, 0 ,-2):
    print(i)


#=================
a = int(input("Enter any number :"))
odd_sum = 0
even_sum = 0
for i in range(1, a+1):
    if i % 2 == 0:
        even_sum += 1
    else:
        odd_sum +=1

print(f"Sum of even numbers up to {number}: {even_sum}")
print(f"Sum of odd numbers up to {number}: {odd_sum}")            




#======================
er = int(input("Enter any number = "))
for i in range(1,5):
    if user == 7:
        print("Congratulation! you are win")
        break
    else:
        user = int(input("Enter any number = "))



#====================
i = 0
while i < 12:
    i = i+1
    if i ==3:
        # continue
        break
    print(i)



#==============================
# num = int(input("Please enter number between 0-50"))
# for i in range(2,50):
#     if num % i == 0 :
#         print("This is not a prime number")
#         break
# else:
#     print("prime number") 
    
# user = int(input("Please enter value"))
# if user == 1:
#         print("This is not a prime number")
# if user > 1:
#         for i in range(2,user):
#                 if user  % i == 0:
#                         print("This is not a prime number")
#                         break
#         else:
#                 print("This is prime number")





    
