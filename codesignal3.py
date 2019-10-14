def checkPalindrome(inputString):
    tempList = inputString.replace("", "")
    i = 0
    if list(inputString) == list(reversed(tempList)):
        return True
    else:
        return False
