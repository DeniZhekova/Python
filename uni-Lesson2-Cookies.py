#Ask the user how many cookies he/she wants to make
amount_cookies = int(input('\nHow many cookies would you like to make: '))

#Ingredient measurements
cookies = 48
sugar = 1.5
butter = 1
flour = 2.75

total_sugar  = (sugar * amount_cookies) / cookies
total_butter = (butter * amount_cookies) / cookies
total_flour  = (flour * amount_cookies) / cookies

#The result
print('\nNumber of cookies =', amount_cookies, end='\n\n')
print('Total sugar =', format(total_sugar, ',.2f'))
print('Total butter =', format(total_butter, ',.2f'))
print('Total flour =', format(total_flour, ',.2f'), end='\n\n')
