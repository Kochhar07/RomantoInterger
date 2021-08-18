def result(n, key):
    dict = {
        1000: 'M', 
        900: 'CM', 
        500: 'D', 
        400: 'CD', 
        100: 'C', 
        90: 'XC', 
        50: 'L', 
        40: 'XL', 
        10: 'X', 
        9: 'IX', 
        5: 'V', 
        4: 'IV', 
        1: 'I'
    }
    return n*dict[key]

arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
n = int(input("Enter number: "))#type casting
x = 0
str = ""
while(n>0):
    q = int(n/arr[x])
    if(q>0):
        str = str + result(q, arr[x])
        n = n % arr[x]
    x=x+1
print(str)