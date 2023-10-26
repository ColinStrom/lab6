'''
Authors: Colin Strom
Purpose: Produce a menu and encode a decoded value by adding 3 to each digit.
Date: 10.25.2023

'''

'''
Author: Claire Wang 
Purpose: Added a decode() function
Date: 10/26/2023
'''

def encode(to_encode):
    encoded_value = ''
    for num in to_encode:
        num = int(num)
        new_value = num + 3
        encoded_value += str(new_value)
    return encoded_value


def decode(to_decode):
    decoded_value = ""
    for num in to_decode:
        num = int(num)
        new_value = num - 3
        decoded_value += str(new_value)
    return decoded_value


def main():
    menu = True
    while menu == True:
        print('Menu\n-------------')
        print('1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!\n')
            encoded_password = encode(password)
        elif option == 2:
            print(f'The encoded passward is {encoded_password}, and the original password is {decode(encoded_password)}.')
        elif option == 3:
            menu = False

if __name__ == '__main__':
    main()