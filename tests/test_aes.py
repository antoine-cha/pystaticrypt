from pystaticrypt.aes import AESCipher


def test_encrypt():
    cipher = AESCipher("key")
    text = "my text is nice"
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    assert isinstance(decrypted, str)
    assert text == decrypted
