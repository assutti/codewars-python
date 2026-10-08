# Return the initials of a two-word name in uppercase, separated by a dot.

def abbrev_name(name):

    words = name.split()

    return f"{words[0][0].upper()}.{words[1][0].upper()}"