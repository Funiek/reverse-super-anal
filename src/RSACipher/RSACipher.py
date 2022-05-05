from sympy import randprime


class RSAKey:

    def __init__(self) -> None:
        super().__init__()
        self.RANGES = (1000, 1200,)

        self.p: int = -1
        self.q: int = -1
        self.n: int = 0
        self.fi: int = 0
        self.e: int = ((1 << 16) + 1)

    def generate_primes(self):
        self.p = randprime(*self.RANGES)
        for i in range(100):
            self.q = randprime(*self.RANGES)
            if self.p != self.q:
                break

        assert self.q != self.p


class RSAPublicKey(RSAKey):
    def __init__(self, n, e) -> None:
        super().__init__()
        self.n = n
        self.e = e

    def __str__(self) -> str:
        return f'RSAPublicKey( n={self.n}, e={self.e} )'

    def decrypt(self, value: int) -> bytes:
        return pow(value, self.e, self.n)


class RSAPrivateKey(RSAKey):

    def __init__(self) -> None:
        super().__init__()

    def create_key(self):
        RSAKey.generate_primes(self)

        self.n = self.q * self.p

        assert self.n != 1

        self.e = self.e
        self.fi = (self.p - 1) * (self.q - 1)
        self.d = pow(self.e, -1, self.fi)

    def get_public_key(self) -> RSAPublicKey:
        return RSAPublicKey(self.n, self.e)

    def __str__(self):
        return f'RSAPrivateKey( n={self.n}, d={self.d} )'

    def encrypt(self, value: int) -> int:
        return pow(value, self.d, self.n)


class RSACipher:
    private_key: RSAPrivateKey
    public_key: RSAPublicKey

    def __init__(self):
        pass

    def initialize(self):
        self.private_key = RSAPrivateKey()
        self.private_key.create_key()
        self.public_key = self.private_key.get_public_key()

    def __str__(self) -> str:
        return f'RSACipher( privateKey={self.private_key}, public_key={self.public_key} )'

    def encrypt(self, value: int) -> bytes:
        return self.private_key.encrypt(value)

    def decrypt(self, value: bytes) -> bytes:
        return self.public_key.decrypt(value)


if __name__ == "__main__":
    rsa_pk = RSAPrivateKey()
    rsa_pk.create_key()
    print(rsa_pk)
    print(rsa_pk.get_public_key())

    rsa_c = RSACipher()
    rsa_c.initialize()
    print(rsa_c)
