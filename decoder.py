'''
Authors: Colin Strom
Purpose: Decode an encoded value by subtracting 3 from each digit.
Date: 10.25.2023
'''

def decode(to_decode):
    decoded_value = ''
    for num in to_decode:
        num = int(num)
        new_value = num - 3
        decoded_value += str(new_value)
    return decoded_value
