class RSAKey:
    p: int
    q: int
    n: int
    fi: int
    e: int
    RANGES: tuple
    def generate_primes(self): ...


class RSAPrivateKey(RSAKey):

    def __init__(self) -> None: ...

    def get_public_key(self): ...


def get_public_key(self): ...


class RSAPublicKey(RSAKey):

    def __init__(self, n: int, e: int) -> None: ...


def rsa_encrypt(encrypt_key: RSAKey): ...


def rsa_decrypt(decrypt_key: RSAKey): ...
