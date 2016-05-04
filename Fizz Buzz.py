def checkio(number):
    b = {0: str(number), 1: "Fizz", 2: "Buzz", 3: "Fizz Buzz"}
    return b[(1 if number % 3 == 0 else 0) + (2 if number % 5 == 0 else 0)]


# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
