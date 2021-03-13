# def fibbo(limit):
#     num1= 0
#     num2= 1
#     count= 0
#     if(limit==0):
#         print(num1)
#     elif(limit==1):
#         print(num1):
#     else:
#         while limit>count:
#             print(num1)
#             nth= num1+num2
#             num1= num2
#             num2= nth
#             count= count+1

# limit= int(input("enter a limit: "))
# fibbo(limit)

# def factorial(number):
#     x= 1
#     if number==1:
#        print("factorial of {} is {}".format(number,number))
        
#     else:
#         for i in range(1,number+1):
#             x= x*i 
#         print("factorial of {} is {}".format(number,x))

# number= int(input("enter a number: "))
# factorial(number)

# def arm(number):
#     sum= 0
#     var= number
#     while var>0:
#         digit= var%10
#         sum= sum+digit**3
#         var= var//10
#     if(number==sum):
#         print("{} is an armstrong number".format(number))
#     else:
#         print("{} is not an armstrong number".format(number))

# number=int(input("enter a number : "))
# arm(number)

# def palin(number):
#     rev= 0
#     var= number
#     while var>0:
#         digit= var%10
#         rev= digit+rev*10
#         var= var//10

#     if(number==rev):
#         print("{} is a plaindrome".format(number))
#     else:
#         print("{} is not a palindrome".format(number))

# number= int(input("enter a number:"))
# palin(number)

# def reversal(string):
#     str=""
#     a= len(string)
#     for i in range(a-1,0,-1):
#         str= str+string[i]
#     print(str)
# string= input("enter you rame: ")
# reversal(string)

# a= [1, 2, 3, 4, 5, 6, 7]
# count= 0
# i= 0
# while i<len(a):
#     count= count+1
#     i= i+1
# print("number of elements are {}".format(count))

# def divisor(number):
#     for i in range(2,number+1):
#         if number%i==0:
#          break
#     print(i)
# number= int(input("enter a number: "))
# divisor(number)

# def gcd(a, b):
#     while b!=0:
#         greatest= b
#         b= a%b
#         a= greatest
#     print(gcd)

# import array as ruds

# var= ruds.array('i', [24, 32, 51, 56, 32, 57, 7, 23])
# # print("before: {}".format(var))
# # print(var)
# var2= ruds.array('i', [])
# l= len(var)
# for i in range(l,0,-1):
#     var2.append(i)
# print(var2)

# i= 0
# count= 0
# while i<l:
#     count= count+1
#     i= i+1
# print(count)

# max= var[0]
# for i in var:
#     if i<max:
#         max= i
# print(max)

# for x in var:
#     if var.count(x)>1:
#         var.pop(x)
# print("after: {}".format(var) )

# for i in range(l-1):
#     for j in range(0, l-i-1):
#         if var[j]<var[j+1]:
#             var[j]=var[j]+var[j+1]
#             var[j+1]=var[j]-var[j+1]
#             var[j]=var[j]-var[j+1]
# k= int(input("k th largest position: "))
# print(var[k-1])

# for i in range(l-1):
#     for j in range(0, l-i-1):
#         if var[j]<var[j+1]:
#             var[j]=var[j]+var[j+1]
#             var[j+1]=var[j]-var[j+1]
#             var[j]=var[j]-var[j+1]
# k= int(input("k th smallest position: "))
# print(var[l-k])

# ...........................................................................................................................
# def arraythreewaypart(lower,upper,n,arr):
#     start= 0
#     end= n-1
#     i= 0
    
#     while i<=end:
#         if arr[i]<lower:
#             temp= arr[i]
#             arr[i]= arr[start]
#             arr[start]= temp
#             i= i+1
#             start= start+1
        
#         elif arr[i]>upper:
#             temp= arr[i]
#             arr[i]= arr[end]
#             arr[end]= temp
#             end= end-1
#         else:
#             i=i+1

# arr=[1,5,10,8,4,2,3,7,0,6,9]
# lower=5
# upper=7
# n= len(arr)

# arraythreewaypart(lower,upper,n,arr)
# print("modified array")
# for i in range(n):
#     print(arr[i], end=" ")


test_list = [3, 6, 7, 8, 9, 2, 1, 5] 
  
# printing original list 
print("The original list : " + str(test_list)) 
  
# using naive method 
# Separating odd and even index elements 
odd_i = [] 
even_i = [] 
for i in range(0, len(test_list)): 
    if i % 2: 
        even_i.append(test_list[i]) 
    else : 
        odd_i.append(test_list[i]) 
  
res = odd_i + even_i 
  
# print result 
print("Seprated odd and even index list: " + str(res)) 