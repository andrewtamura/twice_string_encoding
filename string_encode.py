def encode(words):
    """
    ['foo', 'bar'] -> 'czfooczbar'

    """


    res = []
    for word in words:
        ciphered_length = cipher(len(word))
        res.append(''.join([ciphered_length, 'z', word]))
    return ''.join(res)

def decode(string):
    """
    'czfooczbar' -> ['foo', 'bar']

    """
    res = []
    word_length = 0
    word_length_cipher = []
    word = []

    for char in string:
        if word_length:
            word.append(char)
            word_length -= 1
        else:
            if word:
                res.append(''.join(word))
                word = []
                word_length_cipher = []
            if char is not 'z':
                word_length_cipher.append(char)
            else:
                word_length = decipher(word_length_cipher)
    res.append(''.join(word))
    return res

def cipher(num):
    res = []
    multiple = num / 25
    if multiple:
        for _ in range(multiple):
            res.append('y')
        remainder = num % 25
        if remainder:
            res.append(chr(remainder+96))
    else:
        res.append(chr(num+96))
    return ''.join(res)

def decipher(string):
    res = 0
    for char in string:
        val = ord(char) -96
        res += val

    return res
