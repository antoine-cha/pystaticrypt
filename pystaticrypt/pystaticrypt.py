"""Main module."""

from Crypto.Hash import HMAC, SHA256  # type: ignore

from pystaticrypt.aes import AESCipher


def encrypt(contents: str, password: str) -> str:
    cipher = AESCipher(password)
    encrypted = cipher.encrypt(contents.encode('utf-8'))
    hmac = HMAC.new(password.encode('utf-8'), digestmod=SHA256)
    hmac.update(encrypted)
    return hmac.hexdigest() + encrypted.decode('utf-8')


def decrypt(contents: str, password: str) -> str:
    b_contents = contents.encode('utf-8')
    encrypted_hmac, encrypted_contents = b_contents[:64], b_contents[64:]
    hmac = HMAC.new(password.encode('utf-8'), digestmod=SHA256)
    hmac.update(encrypted_contents)
    decrypted_hmac = hmac.digest()
    if decrypted_hmac != encrypted_hmac:
        raise ValueError(f"Wrong HMAC. {decrypted_hmac} - {encrypted_hmac}")  # type: ignore

    cipher = AESCipher(password)
    decrypted = cipher.decrypt(contents[64:].encode('utf-8')).decode('utf-8')
    return decrypted
