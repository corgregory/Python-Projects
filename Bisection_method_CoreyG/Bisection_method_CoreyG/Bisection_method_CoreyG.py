"""
Implement the Bisection Method
The bisection method, also known as the binary search method, uses a binary search to find the roots of a real-valued function. It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

For example, if the tolerance is 0.01, the bisection method will keep halving the interval until the difference between the upper and lower bounds is less than or equal to 0.01.

In this lab, you will implement a function that uses the bisection method to find the square root of a number.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named square_root_bisection with three parameters:

The number for which you want to find the square root.
The tolerance being the acceptable error margin for the result. You should set a default tolerance value.
The maximum number of iterations to perform. You should set a default number of iterations.
The square_root_bisection function should:

Raise a ValueError with the message Square root of negative number is not defined in real numbers if the number passed to the function is negative.
For numbers 0 and 1, print the message: The square root of [number] is [number] and return the number itself as the square root.
For any other positive number, print the approximate square root with the message: The square root of [square_target] is approximately [root] and return the computed root value.
If no value meets the tolerance condition, print a failure message: Failed to converge within [maximum] iterations and return None.

"""




def square_root_bisection(number, tolerance = 0.01, iterations = 15):
    # Handle negative input: square roots of negative numbers are not real
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    
    # Handle the easy cases: sqrt(0) = 0 and sqrt(1) = 1
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    # Set up the initial interval for the bisection method
    # For numbers > 1, the root lies between 0 and the number
    # For numbers between 0 and 1, the root lies between 0 and 1
    if number > 1:
        lower_bound = 0
        upper_bound = number
    else:
        lower_bound = 0
        upper_bound = 1
    
    # Initialize iteration counter
    counter = 0
    
    # Continue narrowing the interval while:
    # 1. The interval is wider than the tolerance
    # 2. We still have iterations left
    while upper_bound - lower_bound > tolerance and counter < iterations:
        
        # Compute the midpoint of the current interval
        mid_point = (lower_bound + upper_bound) / 2
        
        # Square the midpoint to compare with the target number
        mid_point_squared = mid_point ** 2
        
        # If midpoint^2 is too large, the root must be in the lower half
        if mid_point_squared > number:
            upper_bound = mid_point
        else:
            # Otherwise, the root is in the upper half
            lower_bound = mid_point
        
        # Increment the iteration counter
        counter += 1
    
    # After the loop ends, check if we successfully converged
    if upper_bound - lower_bound <= tolerance:
        # Compute the final midpoint as our approximate root
        mid_point = (lower_bound + upper_bound) / 2
        print(f"The square root of {number} is approximately {mid_point}")
        return mid_point
    else:
        # If we did not converge within the allowed iterations, report failure
        print(f"Failed to converge within {iterations} iterations")
        return None

def main():
    print("Test 1: Perfect square")
    square_root_bisection(9)

    print("\nTest 2: Non-perfect square")
    square_root_bisection(2)

    print("\nTest 3: Small decimal")
    square_root_bisection(0.25)

    print("\nTest 4: Large number")
    square_root_bisection(1000)

    print("\nTest 5: Edge case: 0")
    square_root_bisection(0)

    print("\nTest 6: Edge case: 1")
    square_root_bisection(1)

    print("\nTest 7: Force failure to converge")
    square_root_bisection(50, tolerance=0.000001, iterations=3)

    print("\nTest 8: High precision")
    square_root_bisection(10, tolerance=0.000001, iterations=50)

    print("\nTest 9: Low precision")
    square_root_bisection(10, tolerance=0.5, iterations=10)

    print("\nTest 10: Negative number")
    try:
        square_root_bisection(-4)
    except ValueError as e:
        print("Caught error:", e)



if __name__ == "__main__":
    main()

