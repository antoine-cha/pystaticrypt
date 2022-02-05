from pystaticrypt.aes import AESCipher


def test_encrypt():
    cipher = AESCipher("key")
    text = "my text is nice".encode('utf-8')
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    assert text == decrypted
