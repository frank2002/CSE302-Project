def child_function(a, b, c, d):
    # Perform initial boolean check and use it to influence the computation
    result = (a > b) and not (c > d)

    # Initialize a sum variable
    sum_values = 0

    # Perform various computations inside a while loop with more complexity
    while a < b:
        sum_values += a + c - d
        a += 1
        if a % 2 == 0:  # If 'a' is even
            c += (b % a) << 1
        else:
            d += (b % a) >> 1

        # Use of more boolean operations
        result = result or (sum_values < d)
        if result and sum_values > 50:
            sum_values -= (a * d) % c
        elif not result and sum_values <= 50:
            sum_values += (a + b) // d
        else:
            sum_values *= 2

    # Additional boolean operation for final result
    final_result = result and (sum_values > 100)

    # Final computation to return an integer
    final_computation = (sum_values * a + b - c) if final_result else (sum_values % d)

    return final_computation


def main():
    # Variable definitions
    a = 5
    b = 25
    c = 15
    d = 10

    # Calling child function and storing the result
    result = child_function(a, b, c, d)

    # Print out the result
    print("The result of the child function is:", result)
