import base64

from Crypto.Cipher import AES  # type: ignore
from Crypto.Hash import SHA256  # type: ignore
from Crypto.Protocol.KDF import PBKDF2  # type: ignore
from Crypto.Random import get_random_bytes  # type: ignore
from Crypto.Util.Padding import pad, unpad  # type: ignore


class AESCipher(object):
    def __init__(self, password: str):
        self.password = password
        self.bs = AES.block_size
        self.salt_size = 16
        self.iv_size = 16

    def _get_key(self, salt: bytes) -> bytes:
        key = PBKDF2(self.password, salt, 32, count=1_0000, hmac_hash_module=SHA256)
        return key

    def _gen_salt(self) -> bytes:
        return get_random_bytes(self.salt_size)

    def _gen_iv(self) -> bytes:
        return get_random_bytes(self.iv_size)

    def encrypt(self, raw: bytes) -> bytes:
        raw = pad(raw, self.bs, style='pkcs7')
        salt = self._gen_salt()
        iv = self._gen_iv()
        cipher = AES.new(self._get_key(salt), AES.MODE_CBC, iv)
        return base64.b64encode(salt + iv + cipher.encrypt(raw))

    def decrypt(self, enc: bytes) -> bytes:
        enc = base64.b64decode(enc)
        salt = enc[: self.bs]
        iv = enc[self.bs : 2 * self.bs]
        cipher = AES.new(self._get_key(salt), AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(enc[2 * self.bs :])
        return unpad(decrypted, self.bs, style='pkcs7')
