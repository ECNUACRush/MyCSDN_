S = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#  方便字符转换(超过十进制)

# m进制ton进制 (m进制到10进制，10进制到n进制）
"""
    function declaration:
    :mhex_to_dec(m, origin): m进制到10进制
    :dec_to_nhex(n, origin): 10进制到n进制
    :mhex_to_nhex(m, n, origin): m进制到n进制
"""


def mHex_to_dec(origin, m):
    """

    :param m: Hex(进制， 类型int)
    :param origin: the num to be converted(待转换的数, 类型为str)
    :return: num in Dec(十进制数，类型为str)
    """
    return str(int(origin, base=m))


def dec_to_nhex(origin, n):
    """

    :param n: target Hex(目标进制，类型int)
    :param origin: the num to be converted(待转换的数，类型为str)
    :return: num in nHex(n进制数, 类型str)
    """
    origin = int(origin)
    List = []
    while origin // n:
        List.append(S[origin % n])
        origin //= n
    List.append(S[origin])
    List.reverse()
    List = [str(each) for each in List]  #  把list里的每个int转为str，方便后面join
    return ''.join(List)


def mhex_to_nhex(origin, m, n):
    """

    :param m: origin Hex(原进制，类型int)
    :param n: target Hex(目标进制，类型int）
    :param origin: the num to be converted(待转换的数, 类型str)
    :return: num in nHex(n进制数，类型str)
    """
    dec_num = mHex_to_dec(origin, m)  # type(dec_num) = int
    return dec_to_nhex(dec_num, n)  # return's type: str


if __name__ == '__main__':
    mm, nn = map(int, input().split())  # 在同一行输入当前进制，目标进制
    num_str = input()  # 在第二行输入当前进制下的数
    print(mhex_to_nhex(num_str, mm, nn)) if num_str[0] != '-' else print('-'+mhex_to_nhex(num_str[1::], mm, nn))


