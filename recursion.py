# Recursive Python program to...
# determine how many times a given letter occurs in a string
def countLetter(string, l, i=0, count=0):
    string = string.lower()
    if len(string) > 0 and string[i] == l:
        count += 1
    if i == len(string) - 1 or len(string) == 0:
        return count
    return countLetter(string, l, i+1, count)

# find the Fibonacci series till a specific term
def fibonacciSeries(n, x=0, y=1):
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 0:
        raise ValueError("n must be a positive int")
    if n == 0:
        return
    if x == 0:
        if n == 1:
            return 0
        if n == 2:
            print(0)
            return 1
        print(0)
        print(1)
        n -= 2
    x += y
    y += x
    if n != 0:
        if n == 1:
            return x
        print(x)
        n -= 1
    if n != 0:
        if n == 1:
            return y
        print(y)
    return fibonacciSeries(n-1, x, y)

# find the sum of elements in a list
def sumOfList(arr, i=0):
    if len(arr) == 0:
        return 0
    if i == len(arr) - 1:
        return arr[i]
    return arr[i] + sumOfList(arr, i+1)

# find the binary equivalent of a number
def decToBin(d):
    if type(d) != int:
        raise TypeError("d must be an int")
    if d == 0:
        return 0
    if d == 1:
        return 1
    if d == -1:
        return -1
    return int(str(decToBin(int(d/2))) + str(d%2))

# find the sum of the digits of the number
def sumDigits(n, i=0):
    n = str(n)
    if n[i] == "-":
        i += 1
    if n[i] == ".":
        i += 1
    if i == len(n) - 1:
        if n[0] == "-":
            return -int(n[i])
        return int(n[i])
    if n[0] == "-":
        return -int(n[i]) + sumDigits(n, i+1)
    return int(n[i]) + sumDigits(n, i+1)

# find the LCM of two numbers
def lcm(x, y, i=1):
    x, y = abs(x), abs(y)
    if x == 0 or y == 0:
        return 0
    if x == y:
        return x
    if x > y:
        if i*x % y == 0:
            return int(i * x)
    if x < y:
        if i*y % x == 0:
            return int(i * y)
    return lcm(x, y, i+1)

# find if a number is prime
def prime(n, i=2):
    if type(n) != int:
        raise TypeError("n must be an int")
    if n > 1998:
        raise ValueError("n must be lesser than 1999")
    if n == 2:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n%i == 0:
        return False
    if i == n//2 + 1:
        return True
    return prime(n, i+1)

# find the product of two numbers
def multiply(x, y, a=0):
    if x == 0:
        return 0
    if type(y) == float:
        if type(x) == float:
            raise TypeError("can only accept one float")
        x, y = y, x
    if y < 0:
        return multiply(x, y+1, a-x)
    if y == 0:
        return round(a, 9)
    return multiply(x, y-1, a+x)

# find the power of a number
def power(x, n, a=1):
    if type(n) != int:
        raise TypeError("n must be an int")
    if x == 0 and n == 0:
        raise ZeroDivisionError("power and base cannot both be zero")
    if x == 0:
        return 0
    if n < 0:
        return power(x, n+1, a*(1/x))
    if n == 0:
        return a
    return power(x, n-1, a*x)

# check whether a string is a palindrome
def palindrome(string, i=0):
    if len(string) == 0 or len(string) == 1:
        return True
    string = string.lower()
    if string[i] != string[-(i+1)]:
        return False
    if i == len(string) // 2 - 1:
        return True
    return palindrome(string, i+1)

# reverse a string
def reverse(string, n):
    if n == 0:
        return string
    if n - 1 == 0:
        return string
    return string[n-1] + reverse(string[:-1], n-1)

# flatten a nested list
def flatten(arr, i=0):
    if len(arr) == 0:
        return arr
    if type(arr[i]) == list:
        if len(arr[i]) == 0:
            arr.pop(i)
            i -= 1
        else:
            k = 0
            for j in range(len(arr[i])-1, -1, -1):
                arr.insert(i, arr[i+k][j])
                k += 1
            arr.pop(i+k)
    if type(arr[i]) == list:
        flatten(arr, i)
    if i == len(arr) - 1:
        return arr
    return flatten(arr, i+1)

# find the total sum of a nested list
def flatSum(arr, i=0):
    if len(arr) == 0:
        return 0
    if type(arr[i]) == list:
        if len(arr[i]) == 0:
            arr[i].append(0)
        arr = arr + arr.pop(i)
        return flatSum(arr, i)
    if i == len(arr) - 1:
        return arr[i]
    return arr[i] + flatSum(arr, i+1)

# find the length of a list
def length(arr, l=0):
    try:
        arr[l]
    except IndexError:
        return l
    return length(arr, l+1)