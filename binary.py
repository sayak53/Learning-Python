def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1        
            
arr=[1,2,3,4,5,6,7,7,8,8,8,6,5,43,]
x=int(input('enter the number you want to find:'))
result=binary_search(arr,x)

if(result!= -1):
    print(f'{x} found at index no. {result}')
else:
    print(f'sorry {x} not found!')
