from hashlib import sha1

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from piltover.types import Keys


def get_public_key_fingerprint(public_key: str) -> int:
    # https://core.telegram.org/mtproto/auth_key#dh-exchange-initiation
    # server_public_key_fingerprints is a list of public RSA key fingerprints (64 lower-order bits of SHA1 (server_public_key);

    return int.from_bytes(
        sha1(public_key.strip().encode()).digest()[-64 // 8:],
        byteorder="big",
        signed=False,
    )


def gen_keys():
    # https://dev.to/aaronktberry/generating-encrypted-key-pairs-in-python-69b

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    unencrypted_pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    pem_public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
    )

    private_key = unencrypted_pem_private_key.decode().strip()
    public_key = pem_public_key.decode().strip()

    return Keys(
        private_key=private_key,
        public_key=public_key,
    )


if __name__ == "__main__":
    print(keys := gen_keys())
    print(f"{get_public_key_fingerprint(keys.public_key):x}")
