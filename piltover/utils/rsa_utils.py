import tgcrypto

from hashlib import sha256

from cryptography.hazmat.primitives.asymmetric.types import (
    PRIVATE_KEY_TYPES,
    PUBLIC_KEY_TYPES,
)


"""
RSA_PAD(data, server_public_key) mentioned above is implemented as follows:
    - data_with_padding := data + random_padding_bytes; — where random_padding_bytes are chosen so that the resulting length of data_with_padding is precisely 192 bytes, and data is the TL-serialized data to be encrypted as before. One has to check that data is not longer than 144 bytes.

    - data_pad_reversed := BYTE_REVERSE(data_with_padding); — is obtained from data_with_padding by reversing the byte order.
    a random 32-byte temp_key is generated.

    - data_with_hash := data_pad_reversed + SHA256(temp_key + data_with_padding); — after this assignment, data_with_hash is exactly 224 bytes long.

    - aes_encrypted := AES256_IGE(data_with_hash, temp_key, 0); — AES256-IGE encryption with zero IV.

    - temp_key_xor := temp_key XOR SHA256(aes_encrypted); — adjusted key, 32 bytes

    - key_aes_encrypted := temp_key_xor + aes_encrypted; — exactly 256 bytes (2048 bits) long

    The value of key_aes_encrypted is compared with the RSA-modulus of server_pubkey as a big-endian 2048-bit (256-byte) unsigned integer. If key_aes_encrypted turns out to be greater than or equal to the RSA modulus, the previous steps starting from the generation of new random temp_key are repeated. Otherwise the final step is performed:
    encrypted_data := RSA(key_aes_encrypted, server_pubkey); — 256-byte big-endian integer is elevated to the requisite power from the RSA public key modulo the RSA modulus, and the result is stored as a big-endian integer consisting of exactly 256 bytes (with leading zero bytes if required).
"""


def rsa_decrypt(
    data: bytes, public_key: PUBLIC_KEY_TYPES, private_key: PRIVATE_KEY_TYPES
) -> bytes:
    private = private_key.private_numbers()  # type: ignore
    public = public_key.public_numbers()  # type: ignore

    return pow(
        int.from_bytes(data, "big", signed=False),
        private.d,  # type: ignore
        public.n,  # type: ignore
    ).to_bytes(256, "big", signed=False)


def xor(x: bytes, y: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(x, y))


def rsa_pad_inverse(
    encrypted_data: bytes,
    public_key: PUBLIC_KEY_TYPES,
    private_key: PRIVATE_KEY_TYPES,
) -> bytes:
    key_aes_encrypted = rsa_decrypt(
        encrypted_data,
        public_key=public_key,
        private_key=private_key,
    )
    temp_key_xor = key_aes_encrypted[:32]
    aes_encrypted = key_aes_encrypted[32:]

    temp_key = xor(temp_key_xor, sha256(aes_encrypted).digest())
    data_with_hash = tgcrypto.ige256_decrypt(
        aes_encrypted, temp_key.zfill(32), bytes(32)
    )

    assert (
        len(data_with_hash) == 224
    ), f"Invalid length for data_with_hash (expected 224, got {len(data_with_hash)})"

    data_pad_reversed = data_with_hash[:-32]
    temp_data_hash = data_with_hash[-32:]

    data_with_padding = data_pad_reversed[::-1]
    assert (
        temp_data_hash == sha256(temp_key + data_with_padding).digest()
    ), "Invalid data hash"

    return data_with_padding
