import random
import string


def get_random_string(len=4):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(len))
