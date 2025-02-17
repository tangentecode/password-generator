import string
import random


def gen_printable(size: int) -> str:
    """Generates a password characters that are considered printable by Python with the given length"""
    password: str = ""
    for i in range(size):
        password += random.choice(string.printable)
    return password


def gen_ascii_lower(size: int) -> str:
    """Generate lowercase ascii password with the given length"""
    password: str = ""
    for i in range(size):
        password += random.choice(string.ascii_lowercase)
    return password


def gen_ascii_upper(size: int) -> str:
    """Generate uppecase ascii password with the given length"""
    password: str = ""
    for i in range(size):
        password += random.choice(string.ascii_uppercase)
    return password


def gen_digits(size: int) -> str:
    """Generate only digit password with the given length"""
    password: str = ""
    for i in range(size):
        password += random.choice(string.digits)
    return password


def gen_hex_digits(size: int) -> str:
    """Generate only hexadecimal digit password with the given length"""
    password: str = ""
    for i in range(size):
        password += random.choice(string.hexdigits)
    return password


def gen_punctuation(size: int) -> str:
    """Generate only punctuation password with the given length"""
    password: str = ""
    for i in range(size):
        password += random.choice(string.punctuation)
    return password


def main() -> None:
    """Only for testing purposes"""
    print(gen_ascii_lower(10))
    print(gen_ascii_upper(10))
    print(gen_punctuation(10))
    print(gen_hex_digits(10))


if __name__ == "__main__":
    main()
