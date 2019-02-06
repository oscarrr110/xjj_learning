#coding=utf-8

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    Buzz = []
    for x in range(1, n+1):
        # print(x)
        if x % 3 == 0 and x % 5 != 0:
            Buzz.append("Fizz")
        elif x % 3 == 0 and x % 5 == 0:
            Buzz.append("FizzBuzz")
        elif x % 3 != 0 and x % 5 == 0:
            Buzz.append("Buzz")
        else:
            Buzz.append(str(x))
    return Buzz



if __name__ == "__main__":
    Buzz = fizzBuzz(15)
    print(Buzz)

