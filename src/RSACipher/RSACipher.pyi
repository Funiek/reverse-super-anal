from typing import overload


class RSAKey:
    """ Klasa bazowa dla kluczy RSA

    """
    p: int
    q: int
    n: int
    fi: int
    e: int
    RANGES: tuple
    d: int

    def generate_primes(self):
        """Generowanie liczb pierwszych

        Metoda generująca liczby pierwsze na potrzeby inicjalizacji szyfrowania
        """
        ...


class RSAPrivateKey(RSAKey):
    """Klucz prywatny alg. RSA

    Klucz prywatny służący do odszyfrowywania szyfrogramu.
    """
    def __init__(self) -> None: ...

    def get_public_key(self):
        """Generowanie klucza publiczengo

        Metoda generująca klucz publiczny na podstawie self.
        Jest to jedyna opcja pozyskania klucza publicznego z klucza prywatnego.
        Jest wołana automatycznie przy inicjalizacji klucza prywatnego w RSACipher.
        """
        ...

    def create_key(self):
        """Pozyskanie klucza prywatnego z liczb pierwszych

        Metoda oblicza i przypisuje wartości klucza prywatnego do pól klasy. Bazuje na wygenerowanych wartościach losowych.
        """
        ...

    def decrypt(self, value: bytes) -> bytes:
        """Główna metoda dekrypcji

        Metoda przyjmuje wartości do odszyforwania w reprezentacji binarnej.
        Nastepnie zastosowywuje odpowiednie przekształcenia w celu uzyskania wartości zaszyfrowanego tekstu, również w postaci binarnej.

        :param value: Wartość, która ma być zaszyfrowana.
        :return: Zaszyfrowana wartość w reprezentacji binarnej.
        """
        ...


class RSAPublicKey(RSAKey):
    """Klucz publiczny alg. RSA

    Klucz publiczny służący do zaszyfrowania szyfrogramu.
    """
    def __init__(self, n: int, e: int) -> None: ...

    def encrypt(self, value: bytes) -> bytes:
        """Metoda szyfrują wiadomość z bajtów

        Metoda szyfrująca wiadomość do postaci binarnej z również binarnej. Pozyskany szyfrogram jest zwracany.

        :param value: Wartość binarna do szyfrowania.
        :return: Zaszyfrowana wartość binarna.
        """
        ...


class RSACipher:
    """Klasa szyfru RSA

    Klasa będąca abstrakcją dla procesu szyfrowania i deszyfrowania.
    """
    private_key: RSAPrivateKey
    public_key: RSAPublicKey

    def __init__(self): ...

    def initialize(self):
        """Inicjalizacja szyfru

        Gdy nie zostły podane klucze, nastąpi proces inicjalizacji szyfru, czyli wygenerowanie kluczy.
        """
        ...

    def __str__(self) -> str: ...

    def encrypt(self, value: bytes) -> bytes:
        """ Metoda do szyfrowania RSA.

        :param value: Wartość binarna do zaszyfrowania.
        :return: Zaszyfrowania wartość binarna.
        """
        ...

    def decrypt(self, value: bytes) -> bytes:
        """Metoda do deszyfrowania RSA.

        :param value: Wartość binarna do odszyfrowania.
        :return: Odszyfrowania wartość binarna.
        """
        ...
