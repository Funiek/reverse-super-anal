from src.RSAEncryptor.RSAEncryptor import RSAEncryptor


def main():
    rsa_encryptor = RSAEncryptor()
    print(rsa_encryptor.encrypt_str("123"))
    print(rsa_encryptor.decrypt_str(rsa_encryptor.encrypt_str("123")))

    print()
    print()
    print()

    with open('data.bin', 'rb') as file:
        value = file.read()

    en = rsa_encryptor.encrypt(value)
    print(en)
    de = rsa_encryptor.decrypt(en)
    print(de)

    with open('data.result.bin', 'wb+') as file:
        file.write(de)

    print()
    print()
    print()

    print(rsa_encryptor.encryptor.public_key)
    print(rsa_encryptor.encryptor.private_key)

    with open('data.bin', 'rb') as file:
        value1 = file.read()

    with open('data.result.bin', 'rb') as file:
        value2 = file.read()

    assert value1 == value2

if __name__ == '__main__':
    main()
