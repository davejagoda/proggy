#!/usr/bin/env python3

"""Gemini prompt:
python reads stdin or argument and determines if input is a palindrome

Test input:
"A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps,
snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana
bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a
jar, sore hats, a peon, a canal-- Panama!"

- Guy Steele, CLTL2
"""

import sys


def is_palindrome(text):
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]


def main():
    # 1. Check if command-line arguments were provided
    if len(sys.argv) > 1:
        input_str = " ".join(sys.argv[1:])
    else:
        # 2. Otherwise, read from stdin (e.g., piped input or interactive entry)
        input_str = sys.stdin.read()

    if not input_str.strip():
        print("Error: No input provided.")
        sys.exit(1)

    result = is_palindrome(input_str)
    print(f"Input: {input_str.strip()}")
    print(f"Is Palindrome: {result}")


if __name__ == "__main__":
    main()
