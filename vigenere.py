def generate_key(text, key):
    key = list(key)
    if len(key) == len(text):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(text, key):
    encrypted_text = []
    for i in range(len(text)):
        if text[i].isalpha():  # Hanya mengenkripsi karakter alfabet
            shift = (ord(text[i].upper()) + ord(key[i].upper()) - 2 * ord('A')) % 26
            encrypted_char = chr(shift + ord('A')) if text[i].isupper() else chr(shift + ord('a'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(text[i])  # Tambahkan karakter non-alfabet apa adanya
    return "".join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    for i in range(len(text)):
        if text[i].isalpha():  # Hanya mendekripsi karakter alfabet
            shift = (ord(text[i].upper()) - ord(key[i].upper()) + 26) % 26
            decrypted_char = chr(shift + ord('A')) if text[i].isupper() else chr(shift + ord('a'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(text[i])  # Tambahkan karakter non-alfabet apa adanya
    return "".join(decrypted_text)

def main():
    print("Vigenère Cipher Encrypt & Decrypt")
    text = input("Enter text: ")
    key = input("Enter key: ")

    # Buat kunci yang sesuai panjangnya dengan teks
    key = generate_key(text, key)

    # Pilih mode enkripsi atau dekripsi
    mode = input("Choose mode ('encrypt' or 'decrypt'): ").strip().lower()
    if mode == 'encrypt':
        result = vigenere_encrypt(text, key)
        print(f"Encrypted text: {result}")
    elif mode == 'decrypt':
        result = vigenere_decrypt(text, key)
        print(f"Decrypted text: {result}")
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
