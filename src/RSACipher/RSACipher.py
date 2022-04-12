from sympy import randprime


class RSAKey:
    RANGES = (1000, 1200,)

    p: int = -1
    q: int = -1
    n: int = 0
    fi: int = 0
    e: int = ((1 << 16) + 1)

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


class RSAPrivateKey(RSAKey):

    def __init__(self) -> None:
        super().__init__()
        RSAKey.generate_primes(self)

        self.n = self.q * self.p

        assert self.n != 1

        self.e = self.e
        self.fi = (self.p - 1) * (self.q - 1)
        self.d = pow(self.e, -1, self.fi)

    def get_public_key(self) -> RSAPublicKey:
        return RSAPublicKey(self.n, self.e)

    def __str__(self):
        return f'RSAPrivateKey( p={self.p}, q={self.q} )'


if __name__ == "__main__":
    rsa_pk = RSAPrivateKey()
    print(rsa_pk)
    print(rsa_pk.get_public_key())
