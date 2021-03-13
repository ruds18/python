# def count(shubham):
#     print("no. of integrers are....:)...",len(str(shubham)))

# shubham= int(input("enter a number: "))
# count(shubham)
# .................................................................................................................
# shubh=[1, 2, 3, 3, 443,545, 56]
# Sum= sum(shubh)
# print(Sum)
# ........................................................................................................
# def count(num):
#     c= 0
#     while num!=0:
#         num= num//10
#         c= c+1
#     print(c)

# num= int(input("enter an integer: "))
# count(num)
# .................................................................................................................
# def swap(a, b):
#     temp= a
#     a= b 
#     b= temp
#     print("after swapping a is {}".format(a))
#     print("after swapping b is {}".format(b))


# a= int(input("enter a number"))
# b= int(input("enter another number"))
# print("before swaping a is ", str(a))
# print("before swapping b is ", str(b))
# swap(a, b)
# ......................................................................................................................
def fibb(limit):
    num1= 0
    num2= 1
    count= 0
    if limit==1:
        print(num1)
    elif limit==2:
        print(num2)
    else:
        while count<limit:
            print(num1)
            nth= num1+num2
            num1, num2= num2, nth
            count= count+1

limit= int(input("Enter the limit for the series : "))
fibb(limit)
# .......................................................................................................................
