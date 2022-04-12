class RSAKey:
    ...


    def __init__(self) -> None:
        super().__init__(self)
        ...

    def generate_primes(self): ...


class RSAPrivateKey(RSAKey):
    ...

    def get_public_key(self):
        ...


class RSAPublicKey(RSAKey):
    ...

    def __init__(self, n: int, e: int) -> None:
        ...


def rsa_encrypt(encrypt_key: RSAKey): ...


def rsa_decrypt(decrypt_key: RSAKey): ...
