from flask import Flask, request, jsonify
from cypher.ceasar import CeasarCipher
from cypher.vigenere import VigenereCipher
from cypher.railfence import RailFenceCipher

app = Flask(__name__)

ceasar_cipher = CeasarCipher()
vigenere_cipher = VigenereCipher()
railfence = RailFenceCipher()

@app.route("/api/ceasar/encrypt", methods=['POST'])
def ceasar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = ceasar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/ceasar/decrypt", methods=['POST'])
def ceasar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
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

@app.route("/api/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data["key"]
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

@app.route("/api/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']  # Fixed the key from 'cipher_text' to 'plain_text'
    key = int(data['key'])
    encrypted_text = railfence.rail_fence_encrypt(plain_text, key)  # Fixed the typo in 'encrypted_text'
    return jsonify({'encrypted_text': encrypted_text})  # Corrected 'decrypted_text' to 'encrypted_text'

@app.route("/api/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']  # This is correct as the user would send the encrypted text
    key = int(data['key'])
    decrypted_text = railfence.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
