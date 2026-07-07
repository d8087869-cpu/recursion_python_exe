#1
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base*power(base ,exponent-1)
print(power(2,4))


#2
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)
print(factorial(5))        

#3
def numbers_to_n(n):
    if n == 0:
        return []
    else:
        return numbers_to_n(n -1)+[n]
print(numbers_to_n(5))    

#4
def count_items(lst):
    if lst == []:
        return 0
    else : 
        return 1+ count_items(lst[1:])
print(count_items(['a','b','c']))

#5
def count_evens(numbers):
    if len (numbers) ==0:
        return 0 
    else:
        first = numbers[0]
        rest = numbers[1:]
        if first % 2 == 0:
            return 1 + count_evens(rest)
        else:
            return count_evens(rest)
print(count_evens([4, 7, 10, 3, 8]))        

#6
def max_number(numbers):
    if len (numbers) == 1: 
        return numbers[0]
    else:
        max_rest = max_number(numbers[1:])
        return numbers[0] if numbers[0]> max_rest else max_rest
print(max_number([4, 9, 2, 11, 6]))    


#7
def reverse_string(text):
    if len(text) <=1:
        return text
    else:
        return reverse_string(text[1:])+ text[0]
print(reverse_string('python'))    
#8
def is_palindrome(text):
    if len (text) <=1 : 
        return True
    elif text[0] == text [-1]:
        return is_palindrome(text[1:-1])
    else:
        return False
print(is_palindrome("level")) 
print(is_palindrome("python"))