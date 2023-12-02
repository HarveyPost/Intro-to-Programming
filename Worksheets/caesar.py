def file_caesar_cipher(file, key=88, option='en'):
    with open(file, 'r') as f:
        text = f.read()
    output_text = ""

    for char in text:
        ascii_val = ord(char)
        if ascii_val in range(32, 127):
            char_value = ascii_val + key
            if char_value > 126:
                char_value = (char_value % 127) + 32
            output_text += chr(char_value)
        else:
            output_text += char
    return output_text

print(file_caesar_cipher('plaintext.txt'))
