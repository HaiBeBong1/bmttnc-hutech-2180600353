from flask import Flask, request, jsonify 
from ex01.cipher.caesar import CaesarCipher
from ex01.cipher.vigenere import VigenereCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    if 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key field in request'}), 400
    
    plain_text = data.get('plain_text')
    key = data.get('key')

    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    if 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key field in request'}), 400
    
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    try:
        key = int(key)
    except ValueError:
        return jsonify({'error': 'Key must be an integer'}), 400

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    if 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing plain_text or key field in request'}), 400
    
    plain_text = data.get('plain_text')
    key = data.get('key')

    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    if 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing cipher_text or key field in request'}), 400
    
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)