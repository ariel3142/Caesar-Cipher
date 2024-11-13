def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift  # Membalikkan shift untuk dekripsi

    for char in text:
        if char.isalpha():
            # Menangani huruf kecil dan besar
            offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) + shift - offset) % 26 + offset)
            result += new_char
        else:
            # Karakter non-alfabet tidak berubah
            result += char

    return result

def main():
    print("Caesar Cipher Encrypt & Decrypt")
    text = input("Enter text: ")
    shift = int(input("Enter shift value (1-25): "))
    mode = input("Choose mode ('enkripsi' or 'dekripsi'): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'enkripsi' atau 'dekripsi'.")
        return

    output = caesar_cipher(text, shift, mode)
    print(f"Output ({mode}ed text): {output}")

if __name__ == "__main__":
    main()
