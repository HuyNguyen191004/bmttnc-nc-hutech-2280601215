from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()

app = Flask(__name__)

#Caesar
@app.route("/api/caesar/encrypt", methods = ["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = (data['key'])
    key = int(data['key'])
    encrypted_text = caesar_cipher.caesar_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = (data['key'])
    decrypted_text = caesar_cipher.caesar_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#Vigenere

@app.route("/api/vigenere/encrypt", methods = ["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = (data['key'])
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = (data['key'])
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#RailFence

@app.route("/api/railfence/encrypt", methods = ["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#Playfair
@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfail_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfail_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfail_matrix)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfail_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfail_matrix)
    return jsonify({'decrypted_message': decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
