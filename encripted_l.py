<<<<<<< HEAD
def encrypt_string(text):
    encrypted = []
    for c in text:
        # TODO: Check if `c` is a letter different from 'z' and 'Z'. If so, increment by 1.
        if c.isalpha():
            if c == 'z':
                encrypted.append('a')
            elif c == 'Z':
                encrypted.append('A')
            else:
                encrypted.append(chr(ord(c)+ 1))
        else:
            encrypted.append(c)
        # If 'c' is 'z', change it to 'a'. If 'c' is 'Z', change it to 'A'.
        # Otherwise, keep 'c' unchanged and add it to the encrypted list.
    return ''.join(encrypted)

# Encrypt the string "Hello, Python!" by shifting each letter in the alphabet one by one.
encrypted_text = encrypt_string("Hello, Python!")
=======
def encrypt_string(text):
    encrypted = []
    for c in text:
        # TODO: Check if `c` is a letter different from 'z' and 'Z'. If so, increment by 1.
        if c.isalpha():
            if c == 'z':
                encrypted.append('a')
            elif c == 'Z':
                encrypted.append('A')
            else:
                encrypted.append(chr(ord(c)+ 1))
        else:
            encrypted.append(c)
        # If 'c' is 'z', change it to 'a'. If 'c' is 'Z', change it to 'A'.
        # Otherwise, keep 'c' unchanged and add it to the encrypted list.
    return ''.join(encrypted)

# Encrypt the string "Hello, Python!" by shifting each letter in the alphabet one by one.
encrypted_text = encrypt_string("Hello, Python!")
>>>>>>> b76c48a (Initial commit)
print("The encrypted text is:", encrypted_text) # Should print out "Ifmmp, Qzuipo!"