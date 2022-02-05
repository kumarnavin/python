#Write code to reverse a C-Style String (C-String means that “abcd” is represented as five characters, including the null character )

str = input("Input a string")

str_1 = str

l = len(str)
i = 0
print(l,i)
while (i<=l/2):
    tmp_left = str[i]
    tmp_right = str[l-(i+1)]
    #print("tmp_left", tmp_left, "tmp_right", tmp_right, "1..", str[:i], "2..", str[i+1:l-(i+1)])
    str = str[:i] + tmp_right + str[i+1:l-(i+1)] + tmp_left +  str[l-(i+1):]
    #print(i, ",", str)
    i = i + 1
        
print("new string", str)

new_str = ''
i = len(str_1)-1
while (i>=0):
    new_str = new_str + str_1[i]
    i = i - 1
print("new string", new_str)

