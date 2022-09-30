"""
@Project_Scenario:
    The UGM-27 Polaris is a nuclear missile designed in 1956 - 1960.
    One day Polaris get stuck at the launch point. A Soldier has to
    solve password of launch point, else missile will blow up.

    @Scenario_Knowledge:
    ---> Computer can only generate number between 1 and 100 randomly.
    ---> Soldier has 5 chance to guess the password.

    @Author_Trick:
    ---> Binary Search

@Author:
    Can Ali Ates
"""

# Import Libraries.
import time
import random

# Initialize Password and Chance.
password = random.randint(1, 100)
chance = 5


# Countdown Function.
def countdown(alert):
    print(f"{alert}\nCountdown is Starting...")
    second = 5
    while second > 0:
        print(f"{second}...")
        second -= 1
        time.sleep(1)
    print("Polaris Exploded...")


# Guess the Password.
while True:
    if chance > 0:
        try:
            guess = input("[Password]: ")
            if int(guess) == password:
                print("Password Confirmed. Launch is Aborted.\n")
                break
            else:
                chance = chance - 1
                print(f"Password Denied... {chance} Chance Remained.")
                if chance != 0:
                    print(f"Try {'Higher' if int(guess) < password else 'Lower'} Values...\n")
        except ValueError:
            countdown("\n[Computer]: Wrong Password Format, Access Denied...")
            break
    else:
        countdown("\n[Computer]: All entered passwords rejected. Polaris is launching...")
        break
