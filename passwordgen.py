import random 
import array 

print("Enter the length of the password:")
len=int(input())

dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
					'z'] 

caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
					'Z'] 

symb = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
		'*', '(', ')', '<'] 


list = dig + caps + small + symb 


rand_dig = random.choice(dig) 
rand_caps = random.choice(caps) 
rand_small = random.choice(small) 
rand_symb = random.choice(symb) 

temp_pass = rand_dig + rand_caps + rand_small + rand_symb 


for x in range(len - 4): 
	temp_pass = temp_pass + random.choice(list) 

	
	temp_pass_list = array.array('u', temp_pass) 
	random.shuffle(temp_pass_list) 

password = "" 
for x in temp_pass_list: 
		password = password + x 
print(password) 
