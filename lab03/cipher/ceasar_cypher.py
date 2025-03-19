from ..ceasar.alphabet import ALPHABET  # Make sure the relative import is correct

class CeasarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()  # Convert the text to uppercase
        encrypted_text = []
        for i in text:
            if i in self.alphabet:  # Only process alphabetic characters
                i_index = self.alphabet.index(i)
                output_index = (i_index + key) % alphabet_len  # Add key for encryption
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter)
            else:
                # If it's not an alphabet character, add it as is (e.g., spaces, punctuation)
                encrypted_text.append(i)

        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()  # Convert the text to uppercase
        decrypted_text = []
        for i in text:
            if i in self.alphabet:  # Only process alphabetic characters
                letter_index = self.alphabet.index(i)
                output_index = (letter_index - key) % alphabet_len  # Subtract key for decryption
                output_letter = self.alphabet[output_index]
                decrypted_text.append(output_letter)
            else:
                # If it's not an alphabet character, add it as is (e.g., spaces, punctuation)
                decrypted_text.append(i)

        return "".join(decrypted_text)
