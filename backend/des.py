"""Shared entry points for the Python DES implementation."""

INITIAL_PERMUTATION = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
)

FINAL_PERMUTATION = (
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
)

PC1 = (
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4,
)

PC2 = (
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32,
)

EXPANSION_TABLE = (
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1,
)

P_PERMUTATION = (
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25,
)

S_BOXES = (
    (
        (14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7),
        (0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8),
        (4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0),
        (15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13),
    ),
    (
        (15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10),
        (3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5),
        (0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15),
        (13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9),
    ),
    (
        (10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8),
        (13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1),
        (13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7),
        (1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12),
    ),
    (
        (7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15),
        (13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9),
        (10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4),
        (3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14),
    ),
    (
        (2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9),
        (14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6),
        (4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14),
        (11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3),
    ),
    (
        (12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11),
        (10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8),
        (9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6),
        (4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13),
    ),
    (
        (4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1),
        (13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6),
        (1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2),
        (6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12),
    ),
    (
        (13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7),
        (1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2),
        (7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8),
        (2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11),
    ),
)

KEY_SHIFT_SCHEDULE = (1, 1, 2, 2, 2, 2, 2)


def hex_to_int(hex_string: str) -> int:
    """Convert 1-16 hexadecimal characters to an unsigned 64-bit integer."""
    if not isinstance(hex_string, str):
        raise TypeError("hex value must be a string")
    if not 1 <= len(hex_string) <= 16:
        raise ValueError("hex string must contain 1 to 16 characters")
    if any(character not in "0123456789abcdefABCDEF" for character in hex_string):
        raise ValueError("hex string contains a non-hexadecimal character")
    return int(hex_string, 16)


def int_to_hex(value: int, width: int) -> str:
    """Convert an integer to fixed-width uppercase hexadecimal text."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("value must be an integer")
    if not isinstance(width, int) or isinstance(width, bool):
        raise TypeError("hex width must be an integer")
    if not 1 <= width <= 16:
        raise ValueError("hex width must be between 1 and 16 characters")
    if not 0 <= value < (1 << (width * 4)):
        raise ValueError("value does not fit in the requested hex width")
    return f"{value:0{width}X}"


def validate_and_parse_key(key: str) -> int:
    """Validate a 16-character hexadecimal DES key and return its 64-bit value."""
    if not isinstance(key, str):
        raise TypeError("DES key must be a string")
    if len(key) != 16:
        raise ValueError("DES key must contain exactly 16 hexadecimal characters")
    return hex_to_int(key)


def bytes_to_block(data: bytes) -> int:
    """Convert exactly eight bytes to a big-endian 64-bit DES block."""
    if not isinstance(data, bytes):
        raise TypeError("block data must be bytes")
    if len(data) != 8:
        raise ValueError("a DES block must contain exactly 8 bytes")
    return int.from_bytes(data, byteorder="big")


def block_to_bytes(block: int) -> bytes:
    """Convert an unsigned 64-bit DES block to eight big-endian bytes."""
    if not isinstance(block, int) or isinstance(block, bool):
        raise TypeError("block must be an integer")
    if not 0 <= block < (1 << 64):
        raise ValueError("block must be an unsigned 64-bit value")
    return block.to_bytes(8, byteorder="big")


def rotate_left_28(value: int, shifts: int) -> int:
    """Circularly rotate a 28-bit value to the left."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("rotation value must be an integer")
    if not isinstance(shifts, int) or isinstance(shifts, bool):
        raise TypeError("rotation count must be an integer")
    if not 0 <= value < (1 << 28):
        raise ValueError("rotation value must fit in 28 bits")
    if shifts < 0:
        raise ValueError("rotation count must not be negative")

    shifts %= 28
    if shifts == 0:
        return value
    return ((value << shifts) | (value >> (28 - shifts))) & 0x0FFFFFFF


def generate_round_keys(key: int) -> tuple[int, ...]:
    """Generate the seven 48-bit round keys used by this DES variant."""
    if not isinstance(key, int) or isinstance(key, bool):
        raise TypeError("key must be an integer")
    if not 0 <= key < (1 << 64):
        raise ValueError("key must be an unsigned 64-bit value")

    permuted_key = permute(key, PC1, 64)
    left = (permuted_key >> 28) & 0x0FFFFFFF
    right = permuted_key & 0x0FFFFFFF
    round_keys = []

    for shifts in KEY_SHIFT_SCHEDULE:
        left = rotate_left_28(left, shifts)
        right = rotate_left_28(right, shifts)
        combined = (left << 28) | right
        round_keys.append(permute(combined, PC2, 56))

    return tuple(round_keys)


def sbox_substitution(value: int) -> int:
    """Substitute eight 6-bit chunks through the eight DES S-boxes."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("S-box input must be an integer")
    if not 0 <= value < (1 << 48):
        raise ValueError("S-box input must fit in 48 bits")

    result = 0
    for box_index, s_box in enumerate(S_BOXES):
        shift = 42 - (box_index * 6)
        chunk = (value >> shift) & 0x3F
        row = ((chunk & 0x20) >> 4) | (chunk & 0x01)
        column = (chunk >> 1) & 0x0F
        result = (result << 4) | s_box[row][column]
    return result

def feistel(right: int, round_key: int) -> int:
    """Apply the DES expansion, key mixing, S-boxes, and P permutation."""
    if not isinstance(right, int) or isinstance(right, bool):
        raise TypeError("right half must be an integer")
    if not 0 <= right < (1 << 32):
        raise ValueError("right half must fit in 32 bits")
    if not isinstance(round_key, int) or isinstance(round_key, bool):
        raise TypeError("round key must be an integer")
    if not 0 <= round_key < (1 << 48):
        raise ValueError("round key must fit in 48 bits")

    expanded = permute(right, EXPANSION_TABLE, 32)
    mixed = expanded ^ round_key
    substituted = sbox_substitution(mixed)
    return permute(substituted, P_PERMUTATION, 32)


def des_round(left: int, right: int, round_key: int) -> tuple[int, int]:
    """Apply one DES Feistel round and return the new left and right halves."""
    if not isinstance(left, int) or isinstance(left, bool):
        raise TypeError("left half must be an integer")
    if not 0 <= left < (1 << 32):
        raise ValueError("left half must fit in 32 bits")
    if not isinstance(right, int) or isinstance(right, bool):
        raise TypeError("right half must be an integer")
    if not 0 <= right < (1 << 32):
        raise ValueError("right half must fit in 32 bits")

    new_left = right
    new_right = left ^ feistel(right, round_key)
    return new_left, new_right


def process_block(block: int, round_keys: tuple[int, ...]) -> int:
    """Process one block with seven supplied round keys."""
    if not isinstance(block, int) or isinstance(block, bool):
        raise TypeError("block must be an integer")
    if not 0 <= block < (1 << 64):
        raise ValueError("block must be an unsigned 64-bit value")
    if not isinstance(round_keys, tuple):
        raise TypeError("round keys must be a tuple")
    if len(round_keys) != 7:
        raise ValueError("exactly seven round keys are required")

    permuted_block = permute(block, INITIAL_PERMUTATION, 64)
    left = (permuted_block >> 32) & 0xFFFFFFFF
    right = permuted_block & 0xFFFFFFFF

    for round_key in round_keys:
        left, right = des_round(left, right, round_key)

    preoutput = (right << 32) | left
    return permute(preoutput, FINAL_PERMUTATION, 64)


def encrypt_block(block: int, key: int) -> int:
    """Encrypt one 64-bit block using seven DES rounds."""
    if not isinstance(key, int) or isinstance(key, bool):
        raise TypeError("key must be an integer")
    if not 0 <= key < (1 << 64):
        raise ValueError("key must be an unsigned 64-bit value")
    return process_block(block, generate_round_keys(key))


def decrypt_block(block: int, key: int) -> int:
    """Decrypt one 64-bit block using the seven round keys in reverse order."""
    if not isinstance(key, int) or isinstance(key, bool):
        raise TypeError("key must be an integer")
    if not 0 <= key < (1 << 64):
        raise ValueError("key must be an unsigned 64-bit value")
    return process_block(block, tuple(reversed(generate_round_keys(key))))


def add_padding(data: bytes) -> bytes:
    """Add PKCS#7-style padding for an 8-byte DES block size."""
    if not isinstance(data, bytes):
        raise TypeError("plaintext data must be bytes")
    padding_length = 8 - (len(data) % 8)
    return data + bytes([padding_length]) * padding_length


def remove_padding(data: bytes) -> bytes:
    """Validate and remove 8-byte-block PKCS#7-style padding."""
    if not isinstance(data, bytes):
        raise TypeError("padded data must be bytes")
    if not data or len(data) % 8 != 0:
        raise ValueError("padded data must contain complete 8-byte blocks")

    padding_length = data[-1]
    if not 1 <= padding_length <= 8:
        raise ValueError("invalid padding length")
    if data[-padding_length:] != bytes([padding_length]) * padding_length:
        raise ValueError("invalid padding bytes")
    return data[:-padding_length]


def encrypt_bytes(plaintext: bytes, key: int) -> bytes:
    """Pad and independently encrypt every 8-byte plaintext block."""
    if not isinstance(plaintext, bytes):
        raise TypeError("plaintext must be bytes")

    padded = add_padding(plaintext)
    ciphertext = bytearray()
    for offset in range(0, len(padded), 8):
        block = bytes_to_block(padded[offset:offset + 8])
        ciphertext.extend(block_to_bytes(encrypt_block(block, key)))
    return bytes(ciphertext)


def decrypt_bytes(ciphertext: bytes, key: int) -> bytes:
    """Independently decrypt every 8-byte block and remove padding."""
    if not isinstance(ciphertext, bytes):
        raise TypeError("ciphertext must be bytes")
    if not ciphertext or len(ciphertext) % 8 != 0:
        raise ValueError("ciphertext must contain complete 8-byte blocks")

    padded_plaintext = bytearray()
    for offset in range(0, len(ciphertext), 8):
        block = bytes_to_block(ciphertext[offset:offset + 8])
        padded_plaintext.extend(block_to_bytes(decrypt_block(block, key)))
    return remove_padding(bytes(padded_plaintext))


def bytes_to_hex(data: bytes) -> str:
    """Convert arbitrary bytes to uppercase hexadecimal text."""
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes")
    return data.hex().upper()


def hex_to_bytes(hex_string: str) -> bytes:
    """Validate and convert non-empty, even-length hexadecimal text to bytes."""
    if not isinstance(hex_string, str):
        raise TypeError("hex value must be a string")
    if not hex_string:
        raise ValueError("ciphertext hex must not be empty")
    if len(hex_string) % 2 != 0:
        raise ValueError("hex text must contain an even number of characters")
    if any(character not in "0123456789abcdefABCDEF" for character in hex_string):
        raise ValueError("hex string contains a non-hexadecimal character")
    return bytes.fromhex(hex_string)


def encrypt_text(plaintext: str, key: int) -> str:
    """Encode UTF-8 text, encrypt it, and return uppercase hexadecimal text."""
    if not isinstance(plaintext, str):
        raise TypeError("plaintext must be a string")
    return bytes_to_hex(encrypt_bytes(plaintext.encode("utf-8"), key))


def decrypt_text(ciphertext_hex: str, key: int) -> str:
    """Decrypt hexadecimal ciphertext and decode the plaintext as UTF-8."""
    plaintext = decrypt_bytes(hex_to_bytes(ciphertext_hex), key)
    return plaintext.decode("utf-8")


def permute(value: int, table: tuple[int, ...], input_size: int) -> int:
    """Apply a one-based, MSB-first DES permutation table to an integer."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("value must be an integer")
    if not isinstance(input_size, int) or isinstance(input_size, bool):
        raise TypeError("input size must be an integer")
    if not 1 <= input_size <= 64:
        raise ValueError("input size must be between 1 and 64 bits")
    if not 0 <= value < (1 << input_size):
        raise ValueError("value does not fit in the declared input size")
    if not isinstance(table, tuple):
        raise TypeError("permutation table must be a tuple")
    if not 1 <= len(table) <= 64:
        raise ValueError("permutation table must contain 1 to 64 positions")

    result = 0
    for position in table:
        if not isinstance(position, int) or isinstance(position, bool):
            raise TypeError("permutation positions must be integers")
        if not 1 <= position <= input_size:
            raise ValueError("permutation position is outside the input")
        result = (result << 1) | ((value >> (input_size - position)) & 1)
    return result
