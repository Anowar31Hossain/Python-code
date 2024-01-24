def isPalindrome(x):
    if x < 0:
        return False
    if x == 0:
        return True
    if x % 10 == 0:
        return False
    
    originalx = x
    numberReversed = 0
    while x > 0:
        lastDigit = x % 10
        numberReversed = numberReversed*10 + lastDigit
        x = x // 10

    return numberReversed == originalx


result = isPalindrome(121)
print(result)

