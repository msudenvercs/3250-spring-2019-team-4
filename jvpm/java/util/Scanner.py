def nextInt():
    try:
        user_input = int(input())
        return user_input
    except ValueError:
        raise TypeError("java.util.InputMismatchException")
