def alphabet_position(letter):
    import string
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    if letter in upper:
        count = 0
        for char in upper:
            if char == letter:
                return count
            else:
                count += 1
    if letter in lower:
        count = 0
        for char in lower:
            if char == letter:
                return count
            else:
                count += 1

def rotate_character(char, rot):
    import string
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    space = " "
    if char == space or char in digits or char in symbols:
        return char
    if char in upper:
        return upper[(alphabet_position(char) + rot) % 26]
    if char in lower:
        return lower[(alphabet_position(char) + rot) % 26]

def encrypt(text, rot):
    encrypted_text = ""
    for char in text:
        encrypted_text += rotate_character(char, rot)
    return encrypted_text
