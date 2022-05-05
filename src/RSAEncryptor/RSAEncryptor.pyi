from src.RSACipher.RSACipher import RSACipher, RSAPrivateKey, RSAPublicKey


class RSAEncryptor:
    """Klasa będąca kolejną warstwą abstrakcji

    Fasada klasy RSACipher
    """
    encryptor: RSACipher

    def __init__(self, private_key: RSAPrivateKey = None, public_key: RSAPublicKey = None, *args, **kwargs): ...

    def encrypt(self, message: bytes) -> list:
        """Enkrypcja wartości binarnych

        Metoda szyfruje wartości binarne i następnie zwraca listę liczb reprezentującą szyfrogram.

        :param message: Wiadomość do zaszyfrowania.
        :return: Zaszyfrowana wiadomość w postaci listy intów.
        """
        ...

    def encrypt_str(self, message: str) -> list:
        """Enkrypcja wartości tekstowych

        Metoda szyfruje wartości tekstowe i następnie zwraca listę liczb reprezentującą szyfrogram.

        :param message: Wiadomość do zaszyfrowania.
        :return: Zaszyfrowana wiadomość w postaci listy intów.
        """
        ...

    def decrypt(self, value: list) -> bytes:
        """Dekrypcja wartości do postaci binarnej

        Metoda deszyfruje wartości z listy zawierającą reprezentację szyfrogramu i następnie zwraca odszyfrowaną wiadomość w postaci binarnej.

        :param value: Lista intów reprezentująca wartość szyfrogramu.
        :return: Odszyfrowana wiadomość w postaci binarnej.
        """
        ...

    def decrypt_str(self, value: list) -> str:
        """Dekrypcja wartości do wartości tekstowej

        Metoda deszyfruje wartości z listy zawierającą reprezentację szyfrogramu i następnie zwraca odszyfrowaną wiadomość w postaci tekstowej.

        :param value: Lista intów reprezentująca wartość szyfrogramu.
        :return: Odszyfrowana wiadomość w postaci tekstowej.
        """
        ...
