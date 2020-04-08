# 56 ms, 13.6 MB
def getHint(secret, guess):

    bitmap_secret = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bitmap_guess  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    a_num = 0
    b_num = 0

    for i in range(len(secret)):

        bitmap_secret[int(secret[i])] += 1
        bitmap_guess[int(guess[i])] += 1

        if secret[i] == guess[i]:
            a_num += 1

    for i in range(10):

        b_num += min(bitmap_secret[i], bitmap_guess[i])

    b_num -= a_num

    return "%dA%dB" % (a_num, b_num)
    

# 88 ms, 13.8 MB
def getHint_2(secret, guess):

    bitmap_secret = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bitmap_guess  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    secret = list(map(int, secret))
    guess = list(map(int, guess))

    a_num = 0
    b_num = 0

    for i in range(len(secret)):

        bitmap_secret[secret[i]] += 1
        bitmap_guess[guess[i]] += 1

        if secret[i] == guess[i]:
            a_num += 1

    for i in range(10):

        b_num += min(bitmap_secret[i], bitmap_guess[i])

    b_num -= a_num

    return "%dA%dB" % (a_num, b_num)

# 仅一个bitmap, 可进一步节省空间
# 未通过 secret = "1122" guess = "2211"
def getHint_1(secret, guess):
    '''
    bitmap状态: 0, 1, 2, 3, 用于记录b_num
    角标i代表数字i, 对应元素代表其出现的次数
    0, 两个数组中都没有
    1, guess数组中有
    2, secret数组中有
    3, 两个数组中都有
    '''
    from math import ceil
    bitmap = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   

    len_ = len(secret)
    a_num = 0
    b_num = 0

    for i in range(len_):

        secret_inum = int(secret[i])
        guess_inum = int(guess[i])

        if secret[i] == guess[i]:
            a_num = a_num + 1
        else:
            if (bitmap[secret_inum] % 3) in (0, 1):
                bitmap[secret_inum]  = bitmap[secret_inum] + 2
            if (bitmap[guess_inum] % 3) in (0, 2):
                bitmap[guess_inum] = bitmap[guess_inum] + 1

    for i in range(10):
        b_num += bitmap[i] // 3

    return "%dA%dB" % (a_num, b_num)

    
secret = "1122"
guess =  "2211"

print(getHint(secret, guess))