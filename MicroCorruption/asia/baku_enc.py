# enc.py

from Crypto.Cipher import AES

# 11 keys of size 16 bytes
keys = [
    b'\x7F\x78\x75\xE0\xC9\x77\xD3\x0C\xE8\x5E\xCA\x19\xD0\x22\x11\xF7',
    b'\x4B\x53\x0B\x31\xB5\xCD\x58\xD3\xF5\x9D\xC5\xA9\xC5\x83\xC4\xF3',
    b'\x6F\x1A\xF5\xBB\xFE\x9E\x53\xE2\x40\x50\x9D\x7A\x30\x1E\x01\x5A',
    b'\x62\x59\xA7\x39\x91\x84\xA6\x59\xBE\xCE\xCE\x98\x70\x4E\x9C\x20',
    b'\x53\x93\x45\xA8\xF3\xDD\x01\x60\x2F\x4A\x68\xC1\xCE\x80\x52\xB8',
    b'\x70\x07\x6C\x8B\xA0\x4E\x44\xC8\xDC\x97\x69\xA1\xE1\xCA\x3A\x79',
    b'\xFF\x47\xB0\x2E\xD0\x49\x28\x43\x7C\xD9\x2D\x69\x3D\x5D\x53\xD8',
    b'\xD9\x80\x48\x2F\x2F\x0E\x98\x6D\xAC\x90\x05\x2A\x41\x84\x7E\xB1',
    b'\x7D\xCD\x0F\x8E\xF6\x8E\xD0\x42\x83\x9E\x9D\x47\xED\x14\x7B\x9B',
    b'\xF2\x13\x8F\x14\x8B\x43\xDF\xCC\x75\x10\x4D\x05\x6E\x8A\xE6\xDC',
    b'\x7B\x2F\x0D\x18\x8A\xF1\xFA\x20\x49\x3C\xD2\x51\xF1\x0B\xBC\xB5'
][::-1]

# AES block size (in bytes)
block_size = 16


def s_box(sub_bytes):
    # Perform substitution using the S-Box
    return bytes(s_box[b] for b in sub_bytes)

def encrypt_aes_ecb(plaintext, keys):
    # Create an AES object with ECB mode (no padding)
    cipher = AES.new(keys[0], AES.MODE_ECB)

    # Encrypt the first block
    ciphertext = cipher.encrypt(plaintext[:block_size])

    # Perform round transformation for subsequent blocks
    for i in range(1, len(plaintext) // block_size):
        plaintext_block = plaintext[i * block_size:(i + 1) * block_size]

        # XOR plaintext block with the corresponding key
        xor_block = bytes(p ^ k for (p, k) in zip(plaintext_block, keys[i]))

        # Apply substitution using the S-Box
        sub_bytes = s_box(xor_block)

        # Encrypt the block
        encrypted_block = cipher.encrypt(sub_bytes)

        ciphertext += encrypted_block

    return ciphertext

plaintext = b'ACCESS GRANTED!\x00'  # Replace with your actual plaintext
ciphertext = encrypt_aes_ecb(plaintext, keys)
print(ciphertext.hex())