# Return the average of the numbers in the list, or 0 if the list is empty.

def find_average(numbers):

    if not numbers:
        return 0

    return sum(numbers) / len(numbers)