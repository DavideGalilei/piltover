from hashlib import sha1
from io import BytesIO

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from piltover.types import Keys
from piltover.utils.utils import write_bytes


def get_public_key_fingerprint(public_key: str, signed: bool = False) -> int:
    # https://core.telegram.org/mtproto/auth_key#dh-exchange-initiation
    # server_public_key_fingerprints is a list of public RSA key fingerprints (64 lower-order bits of SHA1 (server_public_key);

    # return int.from_bytes(
    #     sha1(public_key.strip().encode()).digest()[-64 // 8:],
    #     byteorder="big",
    #     signed=False,
    # )
    key = restore_public_key(public_key=public_key)
    num = key.public_numbers() # type: ignore
    n, e = num.n, num.e # type: ignore
    
    n_bytes = n.to_bytes((n.bit_length() + 7) // 8, "big", signed=False)
    e_bytes = e.to_bytes((e.bit_length() + 7) // 8, "big", signed=False)

    buf = BytesIO()
    write_bytes(n_bytes, to=buf)
    write_bytes(e_bytes, to=buf)

    return int.from_bytes(sha1(buf.getvalue()).digest()[-8:], "little", signed=signed)


def restore_private_key(private_key: str):
    return serialization.load_pem_private_key(
        private_key.encode(),
        password=None,
    )


def restore_public_key(public_key: str):
    return serialization.load_pem_public_key(
        public_key.encode(),
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
