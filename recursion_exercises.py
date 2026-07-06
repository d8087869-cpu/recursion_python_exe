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
