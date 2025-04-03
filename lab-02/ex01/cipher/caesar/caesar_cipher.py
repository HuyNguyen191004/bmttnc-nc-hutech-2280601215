from cipher.caesar import ALPHABET
    
class CaesarCipher:
    
    def __init__(self):
        self.alphabet = ALPHABET

<<<<<<< HEAD
    def encrypt_text(self, text:str,key: int)-> str:
=======
    def caesar_encrypt(self, text:str,key: int)-> str:
>>>>>>> 5a215985dc28da89f95ff561c017c341ffc46aba
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            output_lerter = self.alphabet[output_index]
            encrypted_text.append(output_lerter)
        return "".join(encrypted_text)

<<<<<<< HEAD
    def decrypt_text(self, text: str,key: int) -> str:
=======
    def caesar_decrypt(self, text: str,key: int) -> str:
>>>>>>> 5a215985dc28da89f95ff561c017c341ffc46aba
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            lenter_index = self.alphabet.index(letter)
            output_index = (lenter_index - key) % alphabet_len
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)
<<<<<<< HEAD
        return "".join(decrypted_text)
=======
        return "".join(decrypted_text)
    
    
    
>>>>>>> 5a215985dc28da89f95ff561c017c341ffc46aba
