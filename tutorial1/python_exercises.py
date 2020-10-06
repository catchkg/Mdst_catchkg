"""
Intro to python exercises shell code
"""

def is_odd(x):
    if x%2 ==0:
        print("False")
    else:
        print("True")

def is_palindrome(word):
    if word == word[::-1]:
        print(word,"is a palindrome")
    else:
        print(word, "is not a palindrome")

def only_odds(numlist):
    l =[]
    for i in range(len(numlist)):
        if numlist[i]%2 != 0:
            print(numlist[i])

def count_words(text):
    Frequency = dict()
    words = text.split()
    for word in words:
        if word in counts:
            Frequency[word] += 1
        else:
            Freuquency[word] = 1
    return Frequency

