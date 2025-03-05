class VigenereCipher:
    def __init__(self):
        pass

    def _shift_char(self, char, key_char, encrypt=True):
        """Helper method to shift a character based on key_char and mode (encrypt or decrypt)."""
        key_shift = ord(key_char.upper()) - ord('A')
        base = ord('A') if char.isupper() else ord('a')
        shift = key_shift if encrypt else -key_shift
        return chr((ord(char) - base + shift) % 26 + base)

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                encrypted_text += self._shift_char(char, key[key_index % len(key)], encrypt=True)
                key_index += 1
            else:
                encrypted_text += char  # Non-alphabetic characters are added unchanged
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                decrypted_text += self._shift_char(char, key[key_index % len(key)], encrypt=False)
                key_index += 1
            else:
                decrypted_text += char  # Non-alphabetic characters are added unchanged
        return decrypted_text
