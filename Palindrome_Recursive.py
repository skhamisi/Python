#Recursive palindrome function that takes in a string and continually checks to see if the first and last characters of a string match. If the charachters match, then the first and last characters are removed and the functions calls itself again to check the remaining string until there is only one or less characters left. 

def isPalindrome(word):
    #If the length of characters is less than two, the function returns true
    if len(word) <= 1: return True

    #If the first and last characters do not match, then the function returns false
    if word[0] != word[-1]: return False
    #Removes first and last character and checks the remaining string by calling the function again
    return isPalindrome(word[1:-1])

#Allow the user to input a character, string, or integer. 
input = (input('Please enter a word: '))

if isPalindrome(input.lower()):
    print('This word is a palindrome')
else:
    print('This word is not a palindrome')
