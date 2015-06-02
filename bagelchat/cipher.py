import base64

MULTICAST_KEY = 'pvd6dapQQr6xjz9MhoCEaWH4vcfBEj'

def mutlicast_encrypt(plaintext):
    ciphertext = []
    for i in range(len(plaintext)):
        key_c = MULTICAST_KEY[i % len(MULTICAST_KEY)]
        enc_c = chr((ord(plaintext[i]) + ord(key_c)) % 256)
        ciphertext.append(enc_c)
    return base64.urlsafe_b64encode("".join(ciphertext))

def mutlicast_decrypt(ciphertext):
    dec = []
    ciphertext = base64.urlsafe_b64decode(ciphertext)
    for i in range(len(ciphertext)):
        key_c = MULTICAST_KEY[i % len(MULTICAST_KEY)]
        dec_c = chr((256 + ord(ciphertext[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)