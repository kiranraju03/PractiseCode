"""Find the number of pairs of socks from the set of socks

Input : number of socks (n) and array of socks ([])
Output : number of socks pairs available in the array
"""
from collections import Counter

def sockPairChecker(socks):
    socks_count = Counter(socks)
    for eachcount in socks_count:
        sock_color = eachcount
        sock_quantity = socks_count[eachcount]
        #print(sock_color,sock_quantity)
        if sock_quantity == 1:
            print("Socks of color " + str(sock_color) +" is only "+ str(sock_quantity)+ " in number, FIND THE OTHER ONE!")
        elif sock_quantity == 2:
            print("Found a pair of "+str(sock_color))
        elif sock_quantity > 2:
            temp_quantity = sock_quantity
            pair_counter = 0
            while temp_quantity >= 2:
                temp_quantity -= 2
                pair_counter += 1
            if temp_quantity > 0:
                print("Found "+str(pair_counter)+" pairs of socks of color "+str(sock_color)+" and one more extra sock")
            else:
                print("Found " + str(pair_counter) + " pairs of socks of color " + str(sock_color))

sock_array = ['red', 'green', 'red', 'grey', 'blue','red','red','red','red','green']
#sock_array_numbers = [1,1,1,1,3,3,3,2,2,4,4,5,5,6]
sockPairChecker(sock_array)
#sockPairChecker(sock_array_numbers)