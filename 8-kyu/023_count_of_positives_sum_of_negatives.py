# Count positive numbers and sum negative numbers.

def count_positives_sum_negatives(arr):

    if not arr:
        return []

    positives = sum(1 for x in arr if x > 0)
    negatives = sum(x for x in arr if x < 0)

    return [positives, negatives]