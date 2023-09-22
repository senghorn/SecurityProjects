from Crypto.Cipher import AES

with open("ecb-1.bmp", "rb") as f:
    header = f.read(54) # we wanna leave header untouched
    image = f.read()

dec = AES.new("AES128 is secure".encode(), AES.MODE_ECB).decrypt(image)

with open("ecb_image.bmp", "wb") as result:
    result.write(header)
    result.write(dec)