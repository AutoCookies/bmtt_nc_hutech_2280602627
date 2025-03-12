from flask import Flask, render_template, request
from cypher.ceasar import CeasarCipher
from cypher.vigenere import VigenereCipher
from cypher.railfence import RailFenceCipher
from cypher.playfair import PlayFairCipher
from cypher.transposition import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# ----------------------------------------------------------------------------- 

# Caesar Cipher Routes
@app.route("/ceasar")
def ceasar():
    return render_template('ceasar.html')

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    caesar = CeasarCipher()
    encrypted_text = caesar.encrypt_text(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    caesar = CeasarCipher()
    decrypted_text = caesar.decrypt_text(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

# -------------------------------------------------------------------------- 

# Vigenere Cipher Routes
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']

    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']

    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

# -------------------------------------------------------------------------- 

@app.route("/railfence")
def railfence():
    """Render the RailFence cipher page."""
    return render_template('railfence.html')  # Return the HTML template for RailFence cipher

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    """
    Encrypts the given plain text using the RailFence cipher with the given key.

    :param text: The plain text to encrypt.
    :param key: The key to use for encryption.
    :return: The encrypted text.
    """
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)

    # Return the encrypted text with the key and plain text
    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

# ----------------------------------------------------------------------------
@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']

    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)

    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']

    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)

    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

# ----------------------------------------------------------------------------
@app.route('/tranposition')
def transposition():
    return render_template('tranposition.html') 

@app.route("/tranposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])

    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/tranposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])

    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)

    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
