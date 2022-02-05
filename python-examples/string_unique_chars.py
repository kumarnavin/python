import sys
str = input("Input the string")

char_list = []

i = 0
while i<len(str):
    print(str[i])
    if(str[i] in char_list):
        print("Duplicate found")
        sys.exit()
    else:
        char_list.append(str[i])
    i = i + 1
print("String has unique characters")