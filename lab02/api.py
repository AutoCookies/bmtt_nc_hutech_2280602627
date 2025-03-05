from flask import Flask, request, jsonify
from cypher.ceasar import CeasarCipher
from cypher.vigenere import VigenereCipher

app = Flask(__name__)

ceasar_cipher = CeasarCipher()
vigenere_cipher = VigenereCipher()

@app.route("/api/ceasar/encrypt", methods=['POST'])
def ceasar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = ceasar_cipher.encrypt_text(plain_text, key)  # Ensure method matches
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/ceasar/decrypt", methods=['POST'])
def ceasar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']  # Corrected the typo (used '=' instead of '-')
    key = int(data['key'])
    decrypted_text = ceasar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

@app.route("/api/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=['POST'])  # Corrected method to use 'route' for decryption
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data["key"]
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
