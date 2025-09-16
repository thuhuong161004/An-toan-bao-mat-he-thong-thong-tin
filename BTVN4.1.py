def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  
            shift = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - shift + k) % 26 + shift)
        else:
            ciphertext += char  
    return ciphertext

if __name__ == "__main__":
    plaintext = "Ho Thu Huong"  
    k = 5
    ciphertext = caesar_encrypt(plaintext, k)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
