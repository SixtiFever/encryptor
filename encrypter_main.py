""" A PROGRAM TO ENCRYPT AND DECRYPT INPUT MESSAGES """
import random


""" lists to accomodate alphabetic substitution via indexing """
cipher_array = ['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1',
'2','3','4','5','6','7','8','9', '\'','!','@','€','#','$','%','^','&',
'*','(',')','\"',':',';','<',',','.','>','?','/']
cipher_array2 = cipher_array*2

""" key shift to create the randomly generate alphabetic substitution index """
key_shift = random.randint(2,6)

""" function to take input message, and scramble it """
""" 1. take input message. Listify it.
    2. make randome number
    3. Assign each message value a corresponding index in ciper_array
    4. Move values forward by the key_shift
    5. Append and de-list in encrypted message      
"""
def cipher(input_message: str) -> None:
    encrypted_message = list()
    listed_message = input_message.lower()
    for element in listed_message:
        if element in cipher_array:
            original_index = int(cipher_array.index(element))
            shift = original_index + key_shift
            encrypted_message.append(cipher_array2[shift])
        if element == " ":
            encrypted_message.append(element)
    return str(''.join(encrypted_message))


"""
- Take the ciphered message
- Reverse cipher_array2
- For every element in the ciphered message, take element, find index in local array, and move back by the key shit.
Appending to new variable.
- Move the ciphered message back by the key_shit
"""


def decipher(ciphred_message):
    """ function to take the ciphered message, and decrypt it """
    listed_ciphered_msg = list(ciphred_message)  # convert ciphered message to a list
    deciphered_message = list() # creat new list to append to
    reversed_array = sorted(cipher_array, reverse=True) # reverse the array
    local_array = reversed_array*2
    for character in listed_ciphered_msg:  # Loop through ciphered message, get index for each element, apply key shift
        if character != ' ':
            index = local_array.index(character)
            de_shift = index + key_shift
            deciphered_message.append(local_array[de_shift]) # Append to new list
        elif character == ' ':
            deciphered_message.append(' ')
    return str(''.join(deciphered_message))




    

a = cipher('That\'s right!!!')

print(a)
print(decipher(a))



    

    
