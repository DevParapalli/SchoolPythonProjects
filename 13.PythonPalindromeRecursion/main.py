string_to_check = "malayalam"

def isPalindrome(str_obj):
    if len(str_obj) < 1:
        return True
        # blank string is a palindrome
    else:
        if str_obj[0] == str_obj[-1]:
            return isPalindrome(str_obj[1:-1])
        else:
            return False

# this compares individual letters to compare if they are equal, if they are then return true


print(isPalindrome(string_to_check))