"""
Train Seating : Find the seating position(Window, Middle, Aisle Seats) and opposite seat number
in a compartment of 12 seats.

Sample arrangement :
6   7
5   8
4   9

3   10
2   11
1   12

Complexity :
Time : O(1) : No loops, single computation
Space : O(1) : few variables are taken care
"""


def trainSeating(num):
    compartment_total_seats = 12
    seat_guess = num % compartment_total_seats
    # Row 1
    if seat_guess == 1:
        print(str(num + 11) + " Window Seat")
    elif seat_guess == 2:
        print(str(num + 9) + " Middle Seat")
    elif seat_guess == 3:
        print(str(num + 7) + " Aisle Seat")
    elif seat_guess == 4:
        print(str(num + 5) + " Aisle Seat")
    elif seat_guess == 5:
        print(str(num + 3) + " Middle Seat")
    elif seat_guess == 6:
        print(str(num + 1) + " Window Seat")

    # Row 2
    elif seat_guess == 11:
        print(str(num - 9) + " Middle Seat")
    elif seat_guess == 10:
        print(str(num - 7) + " Aisle Seat")
    elif seat_guess == 9:
        print(str(num - 5) + " Aisle Seat")
    elif seat_guess == 8:
        print(str(num - 3) + " Middle Seat")
    elif seat_guess == 7:
        print(str(num - 1) + " Window Seat")

    else:
        print(str(num - 11) + " Window Seat")


if __name__ == "__main__":
    test_cases = int(input("Number of test cases"))
    for each_case in range(test_cases):
        seat_num = int(input("Seat Number to be found"))
        trainSeating(seat_num)
