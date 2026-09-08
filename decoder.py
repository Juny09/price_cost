MAPPING = {
    "E": 1,
    "S": 2,
    "I": 3,
    "N": 4,
    "R": 5,
    "A": 6,
    "M": 7,
    "P": 8,
    "U": 9,
    "T": 10,
    "H": "百位标记",
    "Y": "千位标记",
    "X": "块位标记",
    "0": None,
    "O": None,
}


def decode_code(code):
    code = code.upper()

    result = []

    for char in code:
        if char in MAPPING:
            value = MAPPING[char]

            if value is not None:
                result.append(value)

    return result