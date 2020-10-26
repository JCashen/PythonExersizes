#ATTEMPT 1
print('input first word')
str1 = input()
print('input second word')
str2 = input()
try:
    str1.index(str2)
except ValueError:
    print('False')
else:
    print('True')
