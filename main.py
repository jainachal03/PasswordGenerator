"""
module to generate unique passwords.
-> password will contain smallcase, uppercase and speical symbols(., #, @, &, '(', ')') and numbers {0, 1, 2,...9}
-> password will of length 16
-> password will have equal number of uppercase, lowercase, specials and symbols.

uppercase : [] to contain uppercase characters
lowercase : [] to contain lowercase characters
special   : [] to contain special symbols
numbers   : [] to contain numbers.

"""

import os
import math
import random

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = list(map(lambda  x: x.lower(), uppercase) )

special = ['.', '&', '(', ')', '@', '$', '#']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(map(lambda x: str(x), numbers))

idx_for_upper = random.sample(range(0, 26), 4)
idx_for_lower = random.sample(range(0, 26), 4)
idx_for_special = random.sample(range(0, len(special)), 4)
idx_for_numbers = random.sample(range(0, len(numbers)), 4)

indexes = [idx_for_upper, idx_for_lower, idx_for_special, idx_for_numbers]
lists = [uppercase, lowercase, special, numbers]


def generate():
    password = ""
    idx_for_upper = random.sample(range(0, 26), 4)
    idx_for_lower = random.sample(range(0, 26), 4)
    idx_for_special = random.sample(range(0, len(special)), 4)
    idx_for_numbers = random.sample(range(0, len(numbers)), 4)

    indexes = [idx_for_upper, idx_for_lower, idx_for_special, idx_for_numbers]
    lists = [uppercase, lowercase, special, numbers]

    # important point to understand.
    for idx, listname in zip(indexes, lists):
        for val in idx:
            temp = listname[val]
            password += temp


    l = list(password)
    random.shuffle(l)
    password = ''.join(l)
    return password
