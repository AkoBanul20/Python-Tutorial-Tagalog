#String
pangalan = 'Aaron Jerish Caimbon'
edad = 23
city = 'Quezon City'

''' concatenate ''' 
#print('Ako si ' + pangalan + ', ' + str(edad) + ' taong gulang')

''' String Formatting '''
#Positional Argument
#print('Ako si {name}, {age} taong gulang taga {city}'.format(name=pangalan,age=edad,city='Quezon City'))

#F-String
#print(f'Ako si {pangalan}, {edad} taong gulang taga {city}')


''' String methods '''

BC = 'Welcome To Our Youtube Channel'
#BC.upper()
# BC.lower()
# BC.title()
# BC.swapcase()
# len(BC)
# BC.replace('Our','My')
# BC.count('o')
# BC.startswith('elcome')
# BC.endswith('l')
New_BC = BC.endswith('l')
print(New_BC)


