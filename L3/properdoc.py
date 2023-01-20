def factorial(n):
    """
    Calculates the factorial of a given number.
    :param n: The number to calculate the factorial of.
    :return: The factorial of the given number.
    """
    result = 1
    # Check that the input is a positive integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer")
    # Calculate the factorial
    for i in range(1, n+1):
        result *= i
    return result