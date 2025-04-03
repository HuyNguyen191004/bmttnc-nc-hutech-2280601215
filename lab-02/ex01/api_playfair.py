playfair_cipher = PlayFairCipher()

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