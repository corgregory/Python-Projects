"""
Implement the Luhn Algorithm
The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate a variety of identification numbers, like credit card numbers. These are the steps to validate a number using the Luhn algorithm:

Starting from the right, and excluding the rightmost digit (the check digit), double the value of every other digit.
If the result of doubling a digit is greater than 9, sum the digits to get a single digit. Alternatively, you can subtract 9 from the result.
Take the sum of all the digits including the check digit.
If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
Let's say we have the number 453914881. The steps to validate it using the Luhn algorithm would be:

Example Code
Account number      4   5   3   9   1   4   8   8   1 
Double every other  4  10   3  18   1   8   8  16   1 
Sum 2-char digits   4   1   3   9   1   8   8   7   1 
Then sum all numbers, 4 + 1 + 3 + 9 + 1 + 8 + 8 + 7 + 1 = 42.
Since 42 is not a multiple of 10, the number is invalid.
In this lab, you will build a credit card validator using the Luhn algorithm.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should define a function named verify_card_number that takes a string of digits (representing a card number) and verifies whether it is valid according to the Luhn algorithm.

Within the verify_card_number function:

You should handle any dashes or spaces that may be present in the card number passed to it.
Return VALID! if the card number is valid; otherwise, return INVALID!.


"""




def verify_card_number(card_number: str) -> str:
    """
    Verify a credit card number using the Luhn algorithm.
    Returns 'VALID!' or 'INVALID!'.
    """

    #Clean the input by removing spaces and dashes
    clean_card_number = card_number.replace(" ", "").replace("-", "")

    #Ensure the cleaned string contains only digits
    if not clean_card_number.isdigit():
        return "INVALID!"

    #Convert the cleaned string into a list of integers
    digits = []
    for number in clean_card_number:
        digits.append(int(number))

    #Double every other digit from the right (excluding the check digit)
    for index in range(len(digits) - 2, -1, -2):
        digits[index] *= 2

        # Step 6: If doubling makes a number > 9, subtract 9
        if digits[index] > 9:
            digits[index] -= 9

    #Sum all digits
    total = sum(digits)

    #If total modulo 10 is 0, the card number is valid
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


def main() -> None:

    # Test cases
    print(verify_card_number("4539 1488 0343 6467"))  # VALID
    print(verify_card_number("8273 1232 7352 0569"))  # INVALID example
    print(verify_card_number("1234-5678-9012-3456"))  # INVALID
    print(verify_card_number("49927398716"))          # VALID


if __name__ == "__main__":
    main()
