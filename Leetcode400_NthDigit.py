# Leetcode400_NthDigit.py

def section_length(i):
    # i is the length of digits
    return 9 * i * 10**(i-1)

def section_begin(i):
    # return the first i length digit
    return 1 * 10 ** (i - 1)

def nth(n):
    n -= 1 # 0 based, so we can use % and // correctly
    i = 1
    print('n', n)
    print('i', i)
    while n // section_length(i):
        print('n//section_length(i)', n // section_length(i))
        n -= section_length(i)
        print('n', n)
        i += 1
        print('i')
    sb = section_begin(i)
    print('sb', sb)
    num_full_numbers = n // i
    print('num_full_numbers', num_full_numbers)
    num = sb + num_full_numbers
    pos_in_number = n % i
    return int(str(num)[pos_in_number])


print(nth(3))
