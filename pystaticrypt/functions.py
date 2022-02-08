"""Main module."""

from base64 import b64decode, b64encode
from Crypto.Hash import HMAC, SHA256  # type: ignore

from pystaticrypt.aes import AESCipher


def encrypt(contents: str, password: str) -> str:
    cipher = AESCipher(password)
    encrypted = cipher.encrypt(contents.encode('utf-8'))
    hmac = HMAC.new(password.encode('utf-8'), digestmod=SHA256)
    hmac.update(encrypted)
    return b64encode(hmac.digest() + encrypted).decode('utf-8')


def decrypt(contents: str, password: str) -> str:
    b_contents = b64decode(contents.encode('utf-8'))
    encrypted_hmac, encrypted_contents = b_contents[:32], b_contents[32:]
    hmac = HMAC.new(password.encode('utf-8'), digestmod=SHA256)
    hmac.update(encrypted_contents)
    decrypted_hmac = hmac.digest()
    if decrypted_hmac != encrypted_hmac:
        raise ValueError(f"Wrong HMAC. {decrypted_hmac} - {encrypted_hmac}")  # type: ignore

    cipher = AESCipher(password)
    decrypted = cipher.decrypt(encrypted_contents).decode('utf-8')
    return decrypted
