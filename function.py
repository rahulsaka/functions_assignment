# function to print hello 5 times
'''
def print_hello():
    for i in range(5):
        print("hello")
print("rahul saka")
print_hello()
print("golu")
print_hello()

#Create a function that can accept two arguments name and age and print its value

def x(name,age):
    print(f"the name is {name} and the age is {age}")

x("rahul",29)

 Write a function func1() such that it can accept a variable length of  argument and print all arguments value


#doc_string

print((lambda a:a>5)(6))
'''


def sum(x):
    total = 0
    for i in x:
      total = total + i
    return total
print(sum((8,6,9,)))

def multiplication(y):
    x = 1
    for i in y:
        x *= i
    return x
print(multiplication((8, 2, 3, -1, 7)))

def reverse(x):
    y = x[::-1]
    return y
print(reverse('1234abcd'))

def factorial(z):
    if z == 0:
        return 1
    elif z < 0:
        return "factorials can't be negative"
    else:
        return z * factorial(z-1)

print(factorial(-5))

#Write a Python function to check whether a number is in a given range.

def check_no(x):
    if x in range(0,98):
        return f"{x} is in a range"
    else:
        return  f"{x} is not in range"

print(check_no(8989))

#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'

def check_ULcase(x):
    y = {'Upper_case':0,'Lower_case':0}
    for i in x:
        if i.isupper():
            y['Upper_case']+=1
        elif i.islower():
            y['Lower_case']+=1
        else:
            pass
    print(f"original string is {x}")
    print("no. of upper case is ", y['Upper_case'])
    print("no. of lower case is ", y['Lower_case'])


print(check_ULcase('The quick Brown Fox'))


def unique_no(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

print(unique_no([1,2,3,3,3,3,3,4,4,4,5,5,6,]))


#Write a Python program to print the even numbers from a given list.
#Sample List : Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def evn_no(x):
    y = []
    for i in x:
        if i%2 !=0:
            y.append(i)
    return y

print(evn_no([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def perfect_no(x):
    y = 0
    for i in range(1,x):
        if x%i == 0:
            y += i
    return y == x
#z = int(input("Please enter the no.: "))
'''
print(perfect_no(6))


def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

'''
def palindrome(a):
    x = 0
    y = len(a)-1

    while y>=x:
        if a[x] != a[y]:
            return False
        x+=1
        y-=1
    return True



def palindrme(x):
    y = x[::-1]
    if x == y:
        return 'palindrome no'
    else:
        return 'not a palindrome'



print(palindrme("madam"))



