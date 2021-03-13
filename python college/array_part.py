def arraythreewaypart(lower,upper,n,arr):
    start= 0
    end= n-1
    i= 0
    
    while i<=end:
        if arr[i]<lower:
            temp= arr[i]
            arr[i]= arr[start]
            arr[start]= temp
            i= i+1
            start= start+1
        
        elif arr[i]>upper:
            temp= arr[i]
            arr[i]= arr[end]
            arr[end]= temp
            end= end-1
        else:
            i=i+1

arr=[1,5,10,8,4,2,3,7,0,6,9]
lower=5
upper=7
n= len(arr)

arraythreewaypart(lower,upper,n,arr)
print("modified array")
for i in range(n):
    print(arr[i], end=" ")

# ......................................................................................................

# def partition_array(input, lowVal, highVal):
#    # Separate input list in three parts
#    my_first = [ num for num in input if num<lowVal ]
#    my_second = [ num for num in input if (num>=lowVal and num<=highVal) ]
#    my_third = [ num for num in input if num>highVal ]
#    print(my_first + my_second + my_third)

# my_input = [10, 140, 50, 200, 40, 20, 540, 200, 870, 980, 30, 10, 320]
# my_lowVal = 140
# my_highVal = 200
# partition_array(my_input, my_lowVal, my_highVal)
# .............................................................................................................
4
