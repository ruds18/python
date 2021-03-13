# def swap(a, b):
#     temp= a
#     a= b
#     b= temp
#     print("Affter Swapping: "+str(a))
#     print("Affter Swapping: "+str(b))

# x= int(input("Enter a number to be swapped: "))
# y= int(input("Enter an another number to be swapped: "))
# print("Before swapping: "+str(x))
# print("Before swapping: "+str(y))
# swap(x, y)
# .................................................................................................................
# def count(list):
#     c= 0
#     while c<=len(list)-1:
#         c= c+1
#     print("Number of items present is: {}".format(c))

# li=(1, 2, 3, 4, 5)
# count(li)
# ...................................................................................................................
# def fib(limit):
#     num1= 0
#     num2= 1
#     count= 0
#     if limit==0:
#         print(num1)
#     elif limit==1:
#         print(num1)
#     else:
#         while count<limit:
#             print(num1)
#             nth= num1+ num2
#             num1, num2= num2, nth
#             count= count+1

# li= int(input("Enter limit for series : "))
# fib(li)
# .......................................................................................................................
# def fact(number):
#      x= 1
#      for i in range(1, number+1):
#          x= x*i
#      print(x)

# num= int(input("Enter a number for factorial: "))
# fact(num)
# ..............................................................................................................
# def reversing(number):
#     rev= 0
#     while number>0:
#         rem= number%10
#         rev= rev*10+ rem
#         number= number//10
#     print("reversed number is : "+str(rev))

# num= int(input("Enter a number to be reversed: "))
# reversing(num)
# ...............................................................................................................
# def string_reversal(string):
#     rev= ""
#     x= 0
#     while x<len(string):
#         rev= string[x]+ rev
#         x= x+1
#     print("reversed string: "+ rev)

# string= input("enter a string to be reversed: ")
# string_reversal(string)
# ...............................................................................................................
# def sml_div(number):
#     for x in range(2, number):
#         if(number%x==0):
#             print("smallest divisor of {} is {}".format(number, x))
#             break

# num= int(input("Enter a number for finding its smallest divisor: "))
# sml_div(num)
# ...............................................................................................................
# def greatest(a, b):
#     while b!=0:
#         gcd= num2
#         num2= num1%num2
#         num1= gcd
# ................................................................................................................
# def prime_range(num):
#     if num>1:
#         for num in range(2,num+1):
#             if num>1:
#                 for i in range(2, num):
#                     if(num%i==0):
#                         break
#                     else:
#                         print(num)


# num= int(input("Enter the limit: "))
# prime_range(num)
# .................................................................................................................
# def num(x):
#     for i in range(x):
#         print(i)
#         return

# num(10)
# ....................................................................................................................


         
