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
"0": None,
"O": None,
}

def decode_code(code):
    """
    Decode hidden price code.

    ```
    Examples:
        ESH   -> 120
        ESHYX -> 1200, unit = 块
    """

    code = code.upper().strip()

    number = 0
    unit = None

    for char in code:

        # Ignore 0 and O
        if char in ("0", "O"):
            continue

        # Hundreds marker
        if char == "H":
            number *= 10

        # Thousands marker
        elif char == "Y":
            number *= 10

        # Block/unit marker
        elif char == "X":
            unit = "块"

        # Normal number
        elif char in MAPPING:
            number = number * 10 + MAPPING[char]

        else:
            raise ValueError(f"Invalid character: {char}")

    return {
        "value": number,
        "unit": unit
    }
