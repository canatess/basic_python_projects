"""
@Project_Description:
    A natural number greater than 1 is called a Prime Number if it is divisible
    only by 1 and itself, otherwise it is a Composite Number.

    @Examples:
        3, 5, 7, 11, 13, 17...

@Author:
    Can Ali Ates
"""


# Prime Number Detection Function.
def prime_detector(number):
    is_prime = True
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
    print(f"[Detector]: {'Prime Number' if is_prime else 'Composite Number'}")


# Multiple Queries.
while True:
    try:
        user_input = input("[Number]: ")
        prime_detector(int(user_input))
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
        print("Invalid Character, Please Enter a Valid Number...\n")
