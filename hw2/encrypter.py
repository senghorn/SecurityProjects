""" Encrypts the text using the given key and return the encrypted value.
    Characters and keys must be capitalized. The function will also automatically
    capitalize the characters.
"""
def Vigenere(b, key):
    text = b.replace('\n','').upper()
    text = text.upper()
    key = key.upper()
    length = len(key)
    idx = 0
    encrypted = ""
    for char in text:
        c = ord(char) - 65
        k = ord(key[idx]) - 65
        shifted = (c + k) % 26 + 65
        encrypted += chr(shifted)
        idx = (idx + 1) % length
    return encrypted
