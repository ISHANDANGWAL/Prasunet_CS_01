def decrypt_message(text, key):
    decrypted_text = []
    for ch in text:
        if ch.isalnum():
            # Lowercase characters
            if ch.islower():
                decrypted_ch = chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
            # Uppercase characters
            elif ch.isupper():
                decrypted_ch = chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
            # Numbers
            elif ch.isdigit():
                decrypted_ch = chr((ord(ch) - ord('0') - key + 10) % 10 + ord('0'))
            decrypted_text.append(decrypted_ch)
        elif ch != '\n' and ch != '\r':
            print("Invalid Message")
            return
        else:
            decrypted_text.append(ch)
    
    return ''.join(decrypted_text)

# Taking user input
text = input("Enter a message to decrypt: ")
key = int(input("Enter the key: "))

# Decrypt the message
decrypted_message = decrypt_message(text, key)

if decrypted_message:
    print("Decrypted message:", decrypted_message)
