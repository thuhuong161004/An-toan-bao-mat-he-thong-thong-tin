def text_to_numbers(text):
    numbers = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            numbers.append(ord(ch) - base)
        else:
            numbers.append(ch)  
    return numbers

def numbers_to_text(numbers, template):

    text = ""
    for n, t in zip(numbers, template):
        if isinstance(n, int):
            base = ord('A') if t.isupper() else ord('a')
            text += chr(n + base)
        else:
            text += n
    return text

def encrypt_caesar_z26(plaintext, k):
    nums = text_to_numbers(plaintext)
    encrypted_nums = [(n + k) % 26 if isinstance(n, int) else n for n in nums]
    return numbers_to_text(encrypted_nums, plaintext)

P = "HoThuHuong"
k = 2
C = encrypt_caesar_z26(P, k)

print("Plaintext:", P)
print("Ciphertext:", C)
