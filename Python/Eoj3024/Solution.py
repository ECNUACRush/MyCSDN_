T = int(input())
for i in range(T):
    s = input()[2:]
    print(f'case #{i}:')
    ans, weight = 0, 125  # ans是所求的非0部分, weight为权值
    for ii in s:  # 算出非零部分的值，和CPP版本的思路类似
        ans *= 1000  # 不过由于python的自带高精度，这里直接暴力用int求即可
        ans += int(ii) * weight
        weight *= 125
    a_s, zero = str(ans), ''
    # 例如：0.75 => s = 75 => ans = 7 * 125 * 1000 + 5 * 125 * 125
    # 但实际上真正的值应该是ans / 1000 / 1000
    # 所以我们不难得出结论：前导0的个数 = 原字符串s小数点后位数的长度 * 3 - ans的长度
    lenS, lenA = len(s) * 3, len(a_s)
    for ii in range(lenS - lenA):  # 根据上述结论，补0
        zero += '0'
    a_s = a_s.rstrip('0')  # 题目要求去除后置所有0
    print('0.' + zero + a_s)
