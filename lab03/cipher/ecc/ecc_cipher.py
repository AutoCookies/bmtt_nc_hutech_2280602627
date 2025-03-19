import ecdsa
import os

# Ensure the directory exists
if not os.path.exists('cipher/ecc/keys'):
    os.makedirs("cipher/ecc/keys", exist_ok=True)

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()

        # Save private key
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
        
        # Save public key
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Load private key
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        # Load public key
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
    
        return sk, vk

    def sign(self, message, key):
        # Sign a message with the provided signing key
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        # Verify the signature using the provided public key
        try:
            return key.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False
