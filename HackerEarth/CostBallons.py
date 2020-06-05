"""
Cost of Ballons

Award each participant with green_ballon_cost and blue ballons and find the cost of the ballons bought
Ballons cost is given in each test case, number of participants for each case also given

every case alternatively use blue for first prob and green_ballon_cost for second and swap in the next case

Complexity:
Time : O(N) : N is number of participants
Space : O(1)
"""
test_cases = int(input("Number of test cases : "))

for each_case in range(test_cases):
    print("Case "+str(each_case + 1))

    blue_ballon_cost, green_ballon_cost = map(int, input("Blue and Green Ballons Cost(Spaced) : ").split())
    
    # for each alternative case swap the ballons cost to change the awarding scheme
    if each_case % 2 == 0:
        pass
    else:
        green_ballon_cost, blue_ballon_cost = blue_ballon_cost, green_ballon_cost

    participants_count = int(input("Number of participants : "))

    cost = 0

    for each_participant in range(participants_count):
        # i, j represent the question solved
        i, j = map(int, input("Each participant, Solved 1st or 2nd (1,0 Spaced) : ").split())
        cost += (i * blue_ballon_cost) + (j * green_ballon_cost)

    print(cost)

# Sample Input
# 2
# Case 1
# 9 6
# 10
# 1 1
# 1 1
# 0 1
# 0 0
# 0 1
# 0 0
# 0 1
# 0 1
# 1 1
# 0 0
# Case 2
# 1 9
# 10
# 0 1
# 0 0
# 0 0
# 0 1
# 1 0
# 0 1
# 0 1
# 0 0
# 0 1
# 0 0


# Sample Output :
# 69
# 14