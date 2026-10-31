#!/usr/bin/env python3

"""Gemini prompt 1:
python reads stdin or argument and determines if input is a palindrome

Gemini prompt 2 (did not work):
print the pivot word

Gemini prompt 3:
Modify the python palindrome checker script to print the pivot word in the input

Receved this output:
Input: Never odd or even
Is Palindrome: True
Pivot Word: or

Gemini prompt 4:
Fix bug: "odd" is the pivot word

Test input 1:
'A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps,
snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana
bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a
jar, sore hats, a peon, a canal-- Panama!'

- Guy Steele, CLTL2

Test input 2:
echo 'A man, a plan, a canal Panama' | ./palindrome.py
Input: A man, a plan, a canal Panama
Is Palindrome: True
Pivot Word: canal
"""

import sys


def get_pivot_word(cleaned_words):
    """Finds the word(s) containing the middle character(s)

    of the cleaned palindrome string.
    """
    joined = "".join(cleaned_words)
    if not joined:
        return None

    n = len(joined)
    # Determine middle index/indices of the character string
    if n % 2 == 1:
        mid_indices = [n // 2]
    else:
        mid_indices = [(n // 2) - 1, n // 2]

    # Map character index ranges to their respective original words
    char_to_word = []
    curr = 0
    for w in cleaned_words:
        length = len(w)
        char_to_word.append((curr, curr + length - 1, w))
        curr += length

    # Find which word(s) contain the middle character index/indices
    pivot_words = []
    for mid in mid_indices:
        for start, end, w in char_to_word:
            if start <= mid <= end:
                if w not in pivot_words:
                    pivot_words.append(w)

    return " / ".join(pivot_words)


def is_palindrome(text):
    words = text.split()
    cleaned_words = [
        "".join(char.lower() for char in word if char.isalnum()) for word in words
    ]
    cleaned_words = [w for w in cleaned_words if w]  # Remove empty strings

    if not cleaned_words:
        return False, None

    joined_cleaned = "".join(cleaned_words)
    is_pal = joined_cleaned == joined_cleaned[::-1]

    pivot = get_pivot_word(cleaned_words) if is_pal else None
    return is_pal, pivot


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

    is_pal, pivot = is_palindrome(input_str)

    print(f"Input: {input_str.strip()}")
    print(f"Is Palindrome: {is_pal}")

    if is_pal:
        print(f"Pivot Word: {pivot}")
    else:
        print("Pivot Word: N/A (Not a palindrome)")


if __name__ == "__main__":
    main()
