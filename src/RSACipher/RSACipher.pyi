class RSAKey:
    p: int
    q: int
    n: int
    fi: int
    e: int
    RANGES: tuple
    d: int

    def generate_primes(self): ...


class RSAPrivateKey(RSAKey):

    def __init__(self) -> None: ...

    def get_public_key(self): ...

    def create_key(self): ...

    def encrypt(self): ...


class RSAPublicKey(RSAKey):

    def __init__(self, n: int, e: int) -> None: ...

    def decrypt(self): ...

def rsa_encrypt(encrypt_key: RSAKey): ...


def rsa_decrypt(decrypt_key: RSAKey): ...
