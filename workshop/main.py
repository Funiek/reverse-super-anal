from src.RSAEncryptor.RSAEncryptor import RSAEncryptor


def main():
    rsa_encryptor = RSAEncryptor()
    print(rsa_encryptor.encrypt_str("123"))
    print(rsa_encryptor.decrypt(rsa_encryptor.encrypt_str("123")))

    print(rsa_encryptor.encryptor.public_key)
    print(rsa_encryptor.encryptor.private_key)

if __name__ == '__main__':
    main()
