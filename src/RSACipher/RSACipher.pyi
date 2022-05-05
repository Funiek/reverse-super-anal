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

    def encrypt(self, value: int) -> bytes: ...


class RSAPublicKey(RSAKey):

    def __init__(self, n: int, e: int) -> None: ...

    def decrypt(self, value: bytes) -> bytes: ...


class RSACipher:
    private_key: RSAPrivateKey
    public_key: RSAPublicKey

    def __init__(self): ...

    def initialize(self): ...

    def __str__(self) -> str: ...

    def encrypt(self, value: int) -> bytes: ...

    def decrypt(self, value: int) -> bytes: ...
