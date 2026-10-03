from des import decrypt_text, encrypt_text, validate_and_parse_key


def main() -> None:
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("\nEnter choice: ")

    try:
        if choice == "1":
            plaintext = input("Enter plaintext: ")
            if len(plaintext) > 200:
                raise ValueError("plaintext must not exceed 200 characters")

            key = validate_and_parse_key(input("Enter 16-character hex key: "))
            print(f"\nCiphertext:\n{encrypt_text(plaintext, key)}")
        elif choice == "2":
            ciphertext = input("Enter hexadecimal ciphertext: ")
            if not ciphertext or len(ciphertext) % 16 != 0:
                raise ValueError(
                    "ciphertext must represent complete 8-byte DES blocks"
                )

            key = validate_and_parse_key(input("Enter 16-character hex key: "))
            print(f"\nPlaintext:\n{decrypt_text(ciphertext, key)}")
        else:
            raise ValueError("choice must be 1 or 2")
    except (TypeError, ValueError, UnicodeError) as error:
        print(f"Error: {error}")
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()

# python .\python\main.py  to run this file.