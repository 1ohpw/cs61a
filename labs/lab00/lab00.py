from operator import mul, add
def twenty_eighteen():
    """Come up with the most creative expression that evaluates to 2018,
    using only numbers and the +, *, and - operators.

    >>> twenty_eighteen()
    2018
    """
    one_thousand = pow(10,3)
    two_thousand = mul(2,one_thousand)
    ten = mul(10,1)
    eight = mul(1,8)
    return add(two_thousand, add(ten,eight))
