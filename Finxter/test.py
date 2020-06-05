import numpy as np

# def makeTwoDim(x):
#     if(x.shape) == 1:
#         x = x.reshape(len(x) // 2,2)
#     return x

price1 = [133,132,137]
price2 = [127,140,145]
price3 = [118,118,127]
price4 = [129,131,137]
np.array([[133,132,137],[127,140,145],[118,118,127],[129,131,137]])
np.array([[1.1, 1.2, 1.3],[1.0,1.0,1.0],[0.9,0.8,0.7],[1.1,1.1,1.1]])

a = np.array([price1,price2,price3,price4])
# print(a.shape[0])
# print(a.shape[1])
# # data = np.array(prices)
# #print(data)
# data = makeTwoDim(data)
# print(data)
# print(np.average(data[-1]))

def countingValleys(n, s):
    sea_level = valley = 0
    for i in range(n):
        if (s[i] == 'U'):
            sea_level += 1
            if (sea_level == 0):
                valley += 1
                print(valley)
        else:
            sea_level -= 1

    return valley

print(countingValleys(8,'UDDDUDUU'))

