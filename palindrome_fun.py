#12. Palindrome check....???????
def palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev*10 + n%10
        n //= 10
    return 'Palindrome' if temp==rev else 'Not Palindrome'
print(palindrome(121))
