#1st program
"""a=56
b='90'
d=int(b)
c= a+d
print(c)"""

#2nd program
"""a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

if(a>b):
    print('Greater number is',a)
else:
    print("Gratest number is",b) """   

#3rd program
"""your_name='sayakChakraborty'
a=len(your_name)
b=your_name.endswith('ty')
c=your_name.capitalize()
d=your_name.replace('a','b')
e=your_name.find('a')
f=your_name.count('a')
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)"""

#4th program
"""a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

if(a>b):
    if(a>c):
        print('Largest number is',a)
    else:
        print('largest is',c)
elif(b>c):
    print('largets is',b)
else:
    print('largest is',c)  """   

#5th program
"""a=int(input('enter a number'))
if(a%7==0):
    print('divided by 7')
else:
    print('not divided by 7')"""

#6th program
"""dict = {
    'name':"Superman",
    'actor':"Henry Cavill",
    'money':3785326379563,
    'movies':264,
    'highest paid':145
}
gross ={
    'liked movies':164,
    'moneyGained':74375735
}
print(dict.items())
print(dict.get('actor'))
dict.update(gross)
print(dict)"""

#7th program
"""set1={1,2,3,4,5}
set2={'tony','steve','peter','thor'}
print(set1)
set1.add(6)
set1.remove(6)
set1.pop()
print(set1)
set2.pop()
print(set2)
set3={45,18,10,7}
set4={17,18,12,7,10}
print(set3.union(set4))
print(set3.intersection(set4))"""

#8th program
"""marks=[34,5,6,4,43]
print(marks[1:4])
marks.append(6)
marks.reverse()
marks.insert(3,56)
marks.pop(3)
print(marks)
tup=(1,2,3,4,4,5,5,5,4)
print(tup.count(4))
print(tup.index(5))"""

#9th program
"""i=100
while(i>0):
    print(i)
    i-=1

list=(75,5,45,3,4,45,4543,24)
a=int(input('enter the number you are finding:'))
found =False
for index,numbers in enumerate(list):
    if(numbers==a):
        found=True
        print(f'{a} is found at index no. {index}')
        break
else:
     print('not found')

for i in range(2,102,2):
    print(i)

n=int(input('enter a number'))
for i in range(1,11):
    print(f'{n} x {i} = {n*i}')

n=int(input('enter the number:'))
sum=0
for i in range (1,n+1):
    sum+=i

print(f'The sum of first {n} numbers is : {sum}')

n=int(input('enter the number:'))
sum=1
for i in range (1,n+1):
    sum*=i

print(f'The sum of first {n} numbers is : {sum}')"""

#10th program
def sum(a,b):
    return a+b

print(sum(3,4))

def factorial(n):
    fact=1
    for i in range(1,n+1):
      fact=fact*i
    return fact

print(factorial(5))

def check_prime(n):
    count =0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        print(f'{n} is a prime number')
    else:
        print(f'{n} is not a prime number')

check_prime(45)


def binary_search(arr,target):
    left = 0
    right = len(arr)-1

    while left<=right:
         mid = (left+right) // 2
        
         if arr[mid] == target:
            return mid
         elif arr[mid] < target:
            left = mid + 1
         else:
            right = mid - 1 
      
    return -1 

arr=[1,34,5,6,24,52452,2452,36,34]
target=int(input('Enter the number you wnat  to find'))
result=binary_search(arr,target)

if result!=-1:
    print(f'{target} found at index no. {result}')
else:
    print('sorry not found')