def sum_series(n, first=0, second=1):
    """
    sum_series is a function that calculates the series of values based
    on the first and second values in the series.

    input:
        n that required nth series
        first and second: two integers to determine tpe of series

    example:
        sum_series(6, 2, 1) = 18
        2, 1, 3, 4, 7, 11, 18
    """
    # Base cases
    if n == 0:
        return first
    if n == 1:
        return second

    # Recursive call
    return sum_series(n-1, first, second) + sum_series(n-2, first, second)


if __name__=="__main__":
    sum_series(6, 2, 1)



