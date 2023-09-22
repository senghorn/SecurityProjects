from base64 import b64decode
from Crypto.Cipher import AES

with open("ctr-1.bmp", "rb") as f:
    header = f.read(54) # we wanna leave header untouched
    image = f.read()

dec = AES.new("AES128 is secure".encode(), AES.MODE_CTR, nonce=b64decode("gL297K+02Y0=")).decrypt(image)

with open("ctr_image.bmp", "wb") as result:
    result.write(header)
    result.write(dec)