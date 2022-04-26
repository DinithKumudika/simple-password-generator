import random

print("Welcome to the PyPassword Generator!")

letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number_list = ['0','1','2','3','4','5','6','7','8','9']
symbol_list = ['!','#','$','%','(',')','*','+']

letters = int(input("How many letters would you like in your password?\n")) 
symbols = int(input("How many symbols would you like?\n")) 
numbers = int(input("How many numbers would you like?\n"))

password = []

for letter in range(1,letters + 1):
     rand_letter = random.choice(letter_list)
     password.append(rand_letter)

for symbol in range(1,symbols + 1):
     rand_symbol = random.choice(symbol_list)
     password.append(rand_symbol) 
     
for number in range(1,numbers + 1):
     rand_num = random.choice(number_list)
     password.append(rand_num)
        
for element in password:
     random.shuffle(password)

pwd_str  = ''  

for char in password:
    pwd_str += char

print(f"Generated password: {pwd_str}")
