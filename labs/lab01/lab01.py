"""Lab 1: Expressions and Control Structures"""

# Q3
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0

# Q4
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    # num_digits = 0
    # i = n
    # sum = 0
    # while(n >= 1):
    #     n //= 10
    #     num_digits+=1
    #
    # power_of_ten = pow(10, num_digits - 1)
    # while(power_of_ten >= 1):
    #     digit = i // power_of_ten
    #     sum += digit
    #     i = i % power_of_ten
    #     power_of_ten //= 10

    sum = 0
    while(n >= 1):
        sum += n % 10
        n //= 10
    return sum
