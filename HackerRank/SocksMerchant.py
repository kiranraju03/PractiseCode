"""
Socks Merchant

Find the number of pairs of socks possible from the array of each colored socks represented by the same number

Complexity :
Time : O(N) : N is the size of the array
Space : O(1)
"""

from collections import Counter


def sockMerchant(socks_arr):
    # creating a dict of socks count
    each_sock_count = Counter(socks_arr)

    sock_pairs = 0
    for each_sock in each_sock_count:
        sock_type = each_sock
        sock_quantity = each_sock_count[each_sock]

        if sock_quantity == 1:
            pass
        elif sock_quantity == 2:
            sock_pairs += 1
        elif sock_quantity > 2:
            temp_quant = sock_quantity
            while temp_quant >= 2:
                temp_quant -= 2
                sock_pairs += 1
    return sock_pairs


print(sockMerchant([10, 10, 20, 30, 40, 30, 40, 50, 20]))




