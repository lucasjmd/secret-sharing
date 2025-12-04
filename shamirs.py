import random
from random import randrange, seed

#TODO: Use security safe pseudo-RNG from module 'secrets'

random.seed()

def generate_shares(secret, threshold, shares):
    """
    This function simple coordinate shares to unlock an integer secret at a threshold number of shares.

    :param secret:
    :param threshold:
    :param shares:
    :return:
    """

    secret_coord = tuple([0,secret])

    polynomial_degree = threshold - 1

    coefficients = [secret]

    for i in range(0, polynomial_degree):
        coefficients.append(random.randrange(1, 10))

    print(coefficients)

    share_values = []

    for i in range(1,shares+1):
        x_coord = i
        y_coord = secret
        for degree in range(polynomial_degree, 0, -1):

            y_coord += coefficients[degree]*(x_coord)**degree

        share_value = [x_coord, y_coord]

        share_values.append(tuple(share_value))

    print(share_values)


def byte_converter(string):

    # Get ASCII values of the character

    bytes_string = ''

    for char in string:
        ascii_char = ord(char)
        bytes_char = str(format(ascii_char, '08b'))

        bytes_string += str(bytes_char)

    bit_length = len(bytes_string)

    byte_decimal = 0


    for bit in range(len(bytes_string)-1,-1,-1):
        byte_decimal += int(bytes_string[-(bit+1)]) * 2 ** bit

    return byte_decimal

print(byte_converter('lucas'))

# x = generate_shares(12, 5, 10)











