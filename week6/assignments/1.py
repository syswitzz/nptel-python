import string

letters = list(string.ascii_letters)
password = input("Enter the password string: ")

def count_alphabets(word):
    if not word:
        return 0

    if word[0].isalpha():           
        return 1 + count_alphabets(word[1:])
    else:
        return count_alphabets(word[1:])

n = count_alphabets(password)
print(n)