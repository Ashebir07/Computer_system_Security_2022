###############################################################
## DES - Data Encryption Standard                                   
## Symmetric encryption method based on the fiestal cipher          
## 1. Ashebir wondemeneh 
##  December 2021  
                               
###############################################################
PC_1 = [
            57, 49, 41, 33, 25, 17, 9, 
            1, 58, 50, 42, 34, 26, 18, 
            10, 2, 59, 51, 43, 35, 27, 
            19, 11, 3, 60, 52, 44, 36, 
            63, 55, 47, 39, 31, 23, 15, 
            7, 62, 54, 46, 38, 30, 22, 
            14, 6, 61, 53, 45, 37, 29, 
            21, 13, 5, 28, 20, 12, 4
        ]

PC_2 = [
            14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32
        ]

IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

E_BIT_SELECTION = [
                    32, 1, 2, 3, 4, 5,
                    4, 5, 6, 7, 8, 9,
                    8, 9, 10, 11, 12, 13,
                    12, 13, 14, 15, 16, 17,
                    16, 17, 18, 19, 20, 21,
                    20, 21, 22, 23, 24, 25,
                    24, 25, 26, 27, 28, 29,
                    28, 29, 30, 31, 32, 1
                ]

S_1 = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]

S_2 = [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ]

S_3 = [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ]

S_4 = [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ]

S_5 = [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ]

S_6 = [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ]

S_7 = [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ]

S_8 = [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]

S_BOXES = [S_1, S_2, S_3, S_4, S_5, S_6, S_7, S_8]

P = [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25
    ]

FP = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ] 

SHIFT_NUMBER = [0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

MESSAGE = '0123456789ABCDEF'
KEY = '133457799BBCDFF1'

def hex_to_bin(hex_string):
    bin_string = ''

    for char in hex_string:
        bin_string += bin(int(char, 16))[2:].zfill(4)

    return bin_string

def left_shift(bin_string, shift_by):
    return bin_string[shift_by:] + bin_string[:shift_by]

def xor(bin_1, bin_2):
    xored = ''
    n = len(bin_1)

    for i in range(n):
        if bin_1[i] == bin_2[i]:
            xored += '0'
        else:
            xored += '1'

    return xored


def f_func(r, k_i):
    expanded = ''

    for k in E_BIT_SELECTION:
        expanded += r[k-1]

    k_xor_expanded = xor(expanded, k_i)
    
    split_into_eight = []

    for step in range(0, 48, 6):
        split_into_eight.append(k_xor_expanded[step:step+6])

    s_b = ''

    for i in range(8):
        b_i = split_into_eight[i]
        s_i = S_BOXES[i]
        row = int(b_i[0] + b_i[-1], 2)
        col = int(b_i[1:-1], 2)

        element = bin(s_i[row][col])[2:].zfill(4)

        s_b += element

    f = ''

    for k in P:
        f += s_b[k-1]

    return f

def generate_key(given_key):
    keys_before_perm = []

    key_plus = ''
    bin_key = hex_to_bin(given_key)


    for k in PC_1:
        key_plus += bin_key[k-1]

    c = key_plus[:28]
    d = key_plus[28:]

    for it in range(1, 17):
        c_it = left_shift(c, SHIFT_NUMBER[it])
        d_it = left_shift(d, SHIFT_NUMBER[it])

        keys_before_perm.append(c_it + d_it)

        c = c_it
        d = d_it

    keys_after_perm = [None]

    for key_before_perm in keys_before_perm:
        new_key = ''

        for k in PC_2:
            new_key += key_before_perm[k-1]

        keys_after_perm.append(new_key)

    return keys_after_perm

def encrypt(plain_text, given_key):
    generated_key = generate_key(given_key)

    message_perm = ''
    bin_message = hex_to_bin(plain_text)

    for k in IP:
        message_perm += bin_message[k-1]

    l = message_perm[:32]
    r = message_perm[32:]

    # print(r)
    for it in range(1, 17):
        l_it = r
        r_it = xor(l, f_func(r, generated_key[it]))

        l = l_it
        r = r_it

    r_l = r + l

    bin_encrypted_message = ''

    for k in FP:
        bin_encrypted_message += r_l[k-1]

    encrypted_message = ''

    for step in range(0, 64, 4):
        encrypted_message += hex(int(bin_encrypted_message[step:step+4], 2))[2:].zfill(0).upper()

    return encrypted_message

def decrypt(cipher_text, given_key):
    generated_key = generate_key(given_key)[1:]
    generated_key.reverse()
    generated_key = [None] + generated_key

    cipher_text_perm = ''
    bin_cipher_text = hex_to_bin(cipher_text)

    for k in IP:
        cipher_text_perm += bin_cipher_text[k-1]

    l = cipher_text_perm[:32]
    r = cipher_text_perm[32:]

    for it in range(1, 17):
        l_it = r
        r_it = xor(l, f_func(r, generated_key[it]))

        l = l_it
        r = r_it

    r_l = r + l

    bin_decrypted_message = ''

    for k in FP:
        bin_decrypted_message += r_l[k-1]

    decrypted_message = ''

    for step in range(0, 64, 4):
        decrypted_message += hex(int(bin_decrypted_message[step:step+4], 2))[2:].zfill(0).upper()

    return decrypted_message

encrypted_message = encrypt(MESSAGE, KEY)
decrypted_message = decrypt(encrypted_message, KEY)


print(MESSAGE, encrypted_message, decrypted_message)
