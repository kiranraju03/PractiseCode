"""
Anagrams Checker
"""
anagram_check = lambda first_string, second_string: sorted(first_string) == sorted(second_string)
# Call
print(anagram_check("elivs", "levis"))

"""
Palindrome
"""
palindrome_checker = lambda string_palin: string_palin == string_palin[::-1]
# Call
print(palindrome_checker("nayan"))

"""
Fibonacci
"""
fib_array = [0, 1]
length_of_fib_values = 10
# loop runs to 0 - 'n-2' as already 2 elements are added to the list
[fib_array.append(fib_array[-1] + fib_array[-2]) for i in range(length_of_fib_values - 2)]
print(fib_array)

"""
Factorial
"""
factorial_finder = lambda x: x * factorial_finder(x - 1) if x > 1 else 1
# Call
print(factorial_finder(10))

"""
Rot13 : Rotate 13 : Encryption algorithm : For encrypting a string by shifting 13 characters ahead of its position
"""
all_char = "abcdefghijklmnopqrstuvwxyz"


def rot_13(string_to_be_encrpyted):
    # all_char = "abcdefghijklmnopqrstuvwxyz"
    encrypted_string = ""
    # Moving 13 characters ahead of the pos of existing char and % if the range exceeds the 26 characters
    for each_char in string_to_be_encrpyted:
        encrypted_string += all_char[(all_char.find(each_char) + 13) % 26]

    return encrypted_string

# Single liner
rot_13_singleliner = lambda string_encrypt: "".join([all_char[(all_char.find(each_char) + 13) % 26] for each_char in string_encrypt])
print("Rot13")
print(rot_13("kiranraju"))
print(rot_13_singleliner("kiranraju"))
print(rot_13_singleliner(rot_13_singleliner("kiranraju")))


"""
Sieve of eratosthenes
"""
from functools import reduce

n = 100

primes_list = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2,n)))
print(primes_list)

def sieve(num):
    multiplies = set()
    primes = set()
    for i in range(2, num+1):
        if i not in multiplies:
            primes.add(i)
            for j in range(i*i, n+1, i):
                multiplies.add(j)
    return sorted(primes)
print("Sieve")
print(sieve(100))

"""
Dictionary Comprehension
"""
t = [('Jones', 2.0, 1.0, 8.0)]
totals = {cust : sum(x) for cust, *x in t}
print(totals['Jones'])

"""
Levenshtein_distance 
The Levenshtein distance between two words is the minimum number of single-character edits, 
(insertions, deletions or substitutions) required to change one word into the other.
"""

def leven(a,b):
    if not a : return len(b)
    if not b : return len(a)
    return min( leven(a[1:], b[1:]) + (a[0] != b[0]),
                leven(a[1:], b)+1,
                leven(a, b[1:])+1 )

print("Minimum Edit Distance")
print(leven("kirany", "kiram"))


"""
string Slicing Tricky good
"""
string = "you will get it at once!"
# Keep in mind the end value for slicing
print( string[len(string) : 0 : -1] == string[::-1] )
print(string[len(string)-1: -len(string)-1 : -1] == string[::-1])


"""
print a range of values without using numbers
Hint : ASCII codes
"""
# prints range of values b/w 70 & 80
for i in range(ord('F'), ord('Q')): print(i)

