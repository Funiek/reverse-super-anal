from src.RSACipher.RSACipher import RSAPrivateKey, RSAPublicKey, RSACipher


class RSAEncryptor:
    encryptor: RSACipher

    def __init__(self, private_key: RSAPrivateKey = None, public_key: RSAPublicKey = None, *args, **kwargs):
        self.encryptor = RSACipher()
        self.encryptor.private_key = private_key
        self.encryptor.public_key = public_key

        if self.encryptor.private_key is None:
            self.encryptor.initialize()

        if self.encryptor is not None and self.encryptor.public_key is not None:
            self.encryptor.public_key = self.encryptor.private_key.get_public_key()

        if self.encryptor.private_key is None or self.encryptor.public_key is None:
            raise Exception("Error parsing keys!")

    def encrypt_str(self, message: str) -> list:
        encoded_str = message.encode('utf8')
        return self.encrypt(encoded_str)

    def encrypt(self, values: bytes) -> list:
        return [self.encryptor.encrypt(v) for v in values]

    def decrypt(self, value: list) -> bytes:

        return bytearray([int(self.encryptor.decrypt(v)) for v in value])

    def decrypt_str(self, value: list) -> str:

        return self.decrypt(value).decode()



def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')