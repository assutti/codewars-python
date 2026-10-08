# Remove duplicate values from a list while preserving their original order.
def distinct(seq):
    return list(dict.fromkeys(seq))