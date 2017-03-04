"""
sumTotal = 0
i = 1
while (i<=1001) :
    if ((i+2)%3 == 0) :
        # print (i)
        sumTotal += i
    i += 1

print ("SumTotal is ", sumTotal)

m = 0
for x in range(1,4):
    for y in range(1,3):   
        m = m + 1
print (m)    
    
m = 0
for x in range (1,3):
   for y in range (4,6):
      m = m + x + y
      # print (x,y,m)
print (m)

m = 0
for x in range (1,3):
   k = 0
   for y in range (-2,0):
      k = k + y
      m = m + k
print (m)

m = 0
for x in [3,5,3]:
   for y in range (10,11):
        m = m + x + y
        # print(x,y,m)
print (m)

m = 1
for x in [1,2,3]:
    for y in [3,1,4]:
        if x == y:
            m = m * x 
print (m)

m = 0
my_str_1 = "university"
my_str_2 = "mississipy"
print ("uni" in my_str_1)
"""

def calc_square(x) :
    return x * x

def calc_concat(x) :
    return x + x

"""
#print (calc_square(10))
#print (calc_concat("testing "))


#num_list = [6,5,7,8,3,4]
#num_list = sorted(num_list)
#print (num_list)

char_list = ["x","a"]
char_list = sorted(char_list)
print (char_list)

zipped = list(zip(num_list, char_list))
print (zipped)

num_list_2 = [99,100]
print (sum(num_list) + sum(num_list_2))
"""

def max_fn(input_list) :
    max_val = input_list[0]
    i = 1
    while (i < len(input_list)) :
        if (input_list[i] > max_val) :
            max_val = input_list[i]
        i += 1
    return max_val

"""
num_list = [1,5,8,3,12,-1]
print (max_fn(num_list))
char_list = ["x","a","z","f"]
print (max_fn(char_list))
"""

from math import *
def math_expr_1(x) :
    return abs(x**3) + cos(sqrt(3*x))

def star_display(x) : 
	index = 1
	while (index <= x) :
		star_count = index
		display_char = ""
		#print("inner",display_char, star_count, index)
		while (star_count > 0) :
			display_char = display_char + "*" 
			#print ("innermost", display_char)
			star_count -= 1
		print(display_char)
		index += 1
	while (index > 0) :
		index -= 1
		star_count = index
		display_char = ""
		#print("inner",display_char, star_count, index)
		while (star_count > 1) :
			display_char = display_char + "*" 
			#print ("innermost", display_char)
			star_count -= 1
		print(display_char)

def star_display_1(x) : 
	index = 1
	while (index <= x) :
		star_count = index
		display_char = "*" * index 
		print(display_char)
		index += 1
	while (index > 0) :
		index -= 1
		star_count = index
		display_char = "*" * index 
		print(display_char)
	
def perfect_number(x) :
    i = 1
    y = 0
    while (i < x) :
        if (x%i == 0) :
            y += i
        i += 1
    if (y == x) :
        return True
    else :
        return False
        	
def multiples_list_fn(x) :
    list_x = []
    i = 1
    while (i <= 5) :
        list_x.append(x*i)
        i += 1
    return list_x

def find_n_len_words(input_str, desired_len) :
	words = input_str.split()
	i = 0
	total_matching_words = 0
	while (i < len(words)) :
		if (len(words[i]) == desired_len) :
			total_matching_words = total_matching_words + 1
		i = i + 1
	return total_matching_words
		
def word_count_char_specific(input_str, char) :
	words = input_str.split(" ")
	countChar = 0
	for word in words :
		if word.startswith(char) :
			countChar = countChar + 1
	return countChar

def len_diff_strings(str1, str2):
	return abs(len(str1) - len(str2))

def compare_two_strings(str1, str2):
	if(str1 == str2):
		return 0
	n1 = len(str1)
	n2 = len(str2)
	print(n1)
	print(n2)
	diff = 0
	i = 0
	while(i < min(n1,n2)):
		if(str1[i].lower() != str2[i].lower()):
			diff += 1
		i += 1
	return (diff + len_diff_strings(str1, str2))

def string_manip_one_char(str1, str2):
	if (compare_two_strings(str1, str2) == 1 and len_diff_strings(str1,str2) == 1):
		print ("Two strings only diff by one char for insert/delete to make them match")
	
# End of file







