
"""
check if a digit is palindorome or not
"""

### Iterative version

def iter_palindrome(num):
    reverse_num  = 0
    original_num = num
    while (num!=0):
        remainder = num%10
        reverse_num = reverse_num*10 + remainder
        num/= 10
    is_palin = original_num == reverse_num
    print "{0} is palindrome: {1}".format(original_num, is_palin)

"""
user_num = int(raw_input("num: "))
iter_palindrome(user_num)
"""

# recursive version

def recur_palindrome(r_num, r_reverse=0):
    if r_num == 0:
        return r_reverse
    else:
        r_reminder = r_num % 10
        r_reverse = r_reverse * 10 + r_reminder
        r_num /= 10
        return recur_palindrome(r_num, r_reverse)


num = int(raw_input("num: "))
new_num = recur_palindrome(num)
is_palin = num == new_num
print "{0} is palindrome: {1}".format(new_num, is_palin)
