""" A PROGRAM TO ENCRYPT AND DECRYPT INPUT MESSAGES """
import random

"""
1. Write a message
2. Run the message through the ciper function
3. Store ciphered message in a new object
4. Decrypt the message
"""

cipher_array = ['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher_array2 = cipher_array*2

""" function to take input message, and scramble it """
""" 1. take input message. Listify it.
    2. make randome number
    3. Assign each message value a corresponding index in ciper_array
    4. Move values forward by the key_shift
    5. Append and de-list in encrypted message      
"""
def cipher(input_message: str) -> None:
    x = random.randint(2,6)
    encrypted_message = list()
    listed_message = input_message
    for element in listed_message:
        if element in cipher_array:
            original_index = int(cipher_array.index(element))
            shift = original_index + x
            encrypted_message.append(cipher_array2[shift])
        if element == " ":
            encrypted_message.append(element)
    return str(''.join(encrypted_message))


def decipher()

print(cipher('hello there'))



    

    
