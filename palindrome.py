# Python module script that contains ispalindrome() method to calculate the input string as palindrome string or not .

def ispalindrome(input_string):
    input_string = input_string.casefold()
    return True if list(input_string) == list(reversed(input_string)) else False

def palindrome_string(input_string):
    input_string = input_string.casefold()
    reverse_string = reversed(input_string)
    if list(input_string) == list(reverse_string):
        print("Input string is a Palindrome")
    else:
        print("Input string is not a Palindrome")