def random_alphanum(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits)
                   for _ in range(length))


def digits_from_str(s, length=4):
    """ Returns first n digits from s, starting from beginning.
    Returns false if didn't find n digits

    Parameters
    ----------
    s: string
        the string to extract digits from
    length: int
        number of digits to extract.
    """
    digits = []
    for char in s:
        # omit 0's at beginning
        if char.isdigit() and not (len(digits) == 0 and char == '0'):
            digits.append(char)
        if len(digits) == length:
            return digits
    return False
