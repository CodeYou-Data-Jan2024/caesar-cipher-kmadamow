def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A' ) + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a' ) + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

# Example usage:
text = "I wonder if this will work"
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Original:", text)
print("Encrypted:", encrypted_text)

