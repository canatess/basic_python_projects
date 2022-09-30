"""
@Project_Description:
    When you add each digit of a non-negative integer to the power of the number of digits, and the number
    you get is equal to the original number, the number you get is the Armstrong Number.

    @Examples:
        153 = (1^3) + (5^3) + (3^3)
        1634 = (1^4) + (6^4) + (3^4) + (4^4)

@Author:
    Can Ali Ates
"""


# Armstrong Number Detection Function.
def armstrong_detector(number, number_of_digits):
    result = number
    while number > 0:
        digit = number % 10
        number = number // 10
        result = result - (digit ** number_of_digits)
    print(f"[Detector]: {'True' if (result == 0) else 'False'}")


# Multiple Queries.
while True:
    try:
        user_input = input("[Number]: ")
        armstrong_detector(int(user_input), len(user_input))
        restart = input("\nDo You Want to Try Another Number (Y|N): ")
        if restart == 'Y' or restart == 'y':
            print("Detector Restarting...\n")
            continue
        elif restart == 'N' or restart == 'n':
            print("Logging Out From Detector...\n")
            break
        else:
            print("Invalid Answer, Logging Out From Detector...\n")
            break
    except ValueError:
        print("[Detector]: Invalid Character, Please Enter a Valid Number...\n")