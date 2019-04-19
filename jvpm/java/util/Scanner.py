import os
dir = ""


class Scanner:
    def nextInt(self):
        try:
            user_input = int(input())
        except ValueError:
            raise TypeError("java.util.InputMismatchException")

    def __init__(self):
        # TODO Figure out a nice way to imitate the exception throwing path, in java it shows java.util.InputMismatchException
        print("TODO")


a = Scanner()
a.nextInt()