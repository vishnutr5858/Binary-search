def binary_search(arr,num,data): #arr=given array ;num = total number of index ;data = number searching for

    l=0                          
    r=num-1
    while(l<r):
        mid=(l+r)//2

        if(data==arr[mid]):
            return mid
        elif(data<arr[mid]):
            r=mid-1
        else:
            l=mid+1
    return -1

arr=[2,3,4,5,10,40]
data=14

result= binary_search(arr,5,data)
if(result!=-1):
    print("number is present at index",str(result))
else:
    print("number is not present in the array")    

