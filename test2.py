# Simplified Python program with a main function and a child function as per your instructions.


def child_function(x, y, z):
    result = 0  # Initialize result as an integer.

    # Simple computation using math operations.
    product = x * y
    sum_xy = x + y
    difference = y - x
    quotient = y // x
    remainder = y % x

    # Using a while loop.
    count = z
    while count > 0:
        result = result + 1
        count = count - 1  # Decrement count.

    # Using if-elif-else control.
    if product > 20:
        result = result + quotient
    elif sum_xy < 10:
        result = result + remainder
    else:
        result = result * 2

    # Bitwise operations (shifting).
    left_shift = x << 1
    right_shift = y >> 1

    # Update result with bitwise operations.
    result = result + left_shift
    result = result - right_shift

    # Return an integer result.
    return result


def main():
    # Variable definition
    x = 4  # An integer.
    y = 8  # Another integer.
    z = 3  # Counter for the while loop.

    # Calling child function and print out the result.
    result = child_function(x, y, z)
    print("The result is:", result)


# Execute the main function.
if __name__ == "__main__":
    main()
