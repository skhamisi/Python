def isPalindrome(word):
    palindromeList = []
    if len(word) <= 1: return True
    if[word] != word[-1]: return False
    return isPalindrome(word[1:-1])

isPalindrome('tacocat')