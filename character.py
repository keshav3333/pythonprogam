char = input('enter a character :-  ')

if 'A'<= char <= 'Z':
    print('it is an uppercase character')

elif 'a'<=char <='z':
    print('it is a lower char')

elif '0' <= char <= '9':
    print('it is a digit')

else:
    print('it is a special character')