cipher = "J OBIC KCBZ QOC LGBVV VNGGBPFV BMZ VJYMCZ FS XWK QOC XJMBG SKWUCLQ BMZ KCBZN XWK WFK LWFKVC WM TWZCKM LKNSQWYKBSON"

# Decrypt the caeser cipher
def decrypt_caeser(cipher, shift):
    plain = ""
    for c in cipher:
        if c.isalpha():
            plain += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        else:
            plain += c
    return plain

# Decrypt the substitution cipher
def decrypt_substitution(cipher, key):
    plain = ""
    for c in cipher:
        if c.isalpha():
            plain += chr(key.index(c) + ord('A'))
        else:
            plain += c
    return plain

def char_frequency(cipher):
    freq = {}
    for c in cipher:
        if c.isalpha():
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
    # Sort the dictionary by value
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return freq

# for i in range(1, 26):
#     print(char_frequency(decrypt_caeser(cipher, i)))

print(char_frequency(cipher))
#                                  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" "BPLZCXYOJURGTMWSAKVQFIEHND"
print(decrypt_substitution(cipher, "BALZCFGOJVRENMWPTKSQUIOXYD"))